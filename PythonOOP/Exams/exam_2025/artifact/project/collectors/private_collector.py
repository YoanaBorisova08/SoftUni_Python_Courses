from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    def __init__(self, name: str):
        super().__init__(name, 25000.0, 3000)

    @property
    def increase_amount(self) -> float:
        return 5000.0