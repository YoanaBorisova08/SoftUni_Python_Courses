from abc import ABC, abstractmethod
import re
from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: list[BaseAstronaut] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not re.match(r"^[0-9a-zA-Z/-]+$", value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value<0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value


    def calculate_total_salaries(self):
        total_salaries = 0
        total_salaries += sum(astronaut.salary for astronaut in self.astronauts)
        return f"{total_salaries:.2f}"

    def status(self):
        sorted_astronauts = sorted(self.astronauts, key=lambda x: x.id_number)
        result = (f"Station name: {self.name}; "
                  f"Astronauts: {' #'.join(a.id_number for a in sorted_astronauts) if self.astronauts else 'N/A'}; "
                  f"Total salaries: {self.calculate_total_salaries()}")
        return result
    @abstractmethod
    def update_salaries(self, min_value: float):
        pass

    def add_astronaut(self, astronaut: BaseAstronaut):
        if self.capacity >0:
            self.astronauts.append(astronaut)
            self.capacity -= 1

    def remove_astronaut(self, astronaut: BaseAstronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)
            self.capacity += 1