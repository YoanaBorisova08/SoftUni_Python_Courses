import re
from abc import ABC, abstractmethod

from project.artifacts.base_artifact import BaseArtifact


class BaseCollector(ABC):
    def __init__(self, name: str, available_money: float, available_space: int):
        self.name = name
        self.available_money = available_money
        self.available_space = available_space
        self.purchased_artifacts:list[BaseArtifact] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not re.match(r'^[A-Za-z0-9][A-Za-z0-9 ]*[A-Za-z0-9]$', value):
            raise ValueError("Collector name must contain letters, numbers, and optional white spaces between them!")
        self.__name = value

    @property
    def available_money(self):
        return self.__available_money

    @available_money.setter
    def available_money(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative amount of money!")
        self.__available_money = value

    @property
    def available_space(self):
        return self.__available_space

    @available_space.setter
    def available_space(self, value):
        if value < 0:
            raise ValueError("A collector cannot have a negative space available for exhibitions!")
        self.__available_space = value

    @property
    @abstractmethod
    def increase_amount(self) -> float:
        pass

    def increase_money(self):
        self.available_money += self.increase_amount

    def can_purchase(self, artifact_price: float, artifact_space_required: int):
        if artifact_price > self.available_money or artifact_space_required > self.available_space:
            return False
        return True

    def __str__(self):
        result = (f"Collector name: {self.name}; Money available: {self.available_money:.2f}; "
                  f"Space available: {self.available_space}; Artifacts: ")
        if self.purchased_artifacts:
            sorted_artifacts_names = sorted((artifact.name for artifact in self.purchased_artifacts), reverse=True)
            result += ", ".join(sorted_artifacts_names)
        else:
            result += "none"

        return result



