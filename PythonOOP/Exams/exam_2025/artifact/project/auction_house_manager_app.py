from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        VALID_ARTIFACTS: dict[str, type[BaseArtifact]] = {
            "RenaissanceArtifact": RenaissanceArtifact,
            "ContemporaryArtifact": ContemporaryArtifact
        }

        if artifact_type not in VALID_ARTIFACTS:
            raise ValueError("Unknown artifact type!")

        if next((a for a in self.artifacts if a.name == artifact_name), None):
            raise ValueError(f"{artifact_name} has been already registered!")

        self.artifacts.append(VALID_ARTIFACTS[artifact_type](artifact_name, artifact_price, artifact_space))
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        VALID_COLECTORS: dict[str, type[BaseCollector]] = {
            "PrivateCollector": PrivateCollector,
            "Museum": Museum
        }

        if collector_type not in VALID_COLECTORS:
            ValueError("Unknown collector type!")

        if next((c for c in self.collectors if c.name == collector_name), None):
            raise ValueError(f"{collector_name} has been already registered!")

        self.collectors.append(VALID_COLECTORS[collector_type](collector_name))
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
       collector = next((c for c in self.collectors if c.name == collector_name), None)
       if collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

       artifact = next((a for a in self.artifacts if a.name == artifact_name), None)
       if artifact is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

       if not collector.can_purchase(artifact.price, artifact.space_required):
           return "Purchase is impossible."

       self.artifacts.remove(artifact)
       collector.purchased_artifacts.append(artifact)
       collector.available_money -= artifact.price
       collector.available_space -= artifact.space_required
       return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)
        if artifact is None:
            return "No such artifact."

        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        collectors_increased = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                collectors_increased += 1

        return f"{collectors_increased} collector/s increased their available money."

    def get_auction_report(self):
        total_sold_artifacts = sum(len(c.purchased_artifacts) for c in self.collectors)
        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name))
        result = (f"**Auction statistics**\n"
                  f"Total number of sold artifacts: {total_sold_artifacts}\n"
                  f"Available artifacts for sale: {len(self.artifacts)}\n***")
        for collector in sorted_collectors:
            result += f"\n{str(collector)}"
        return result