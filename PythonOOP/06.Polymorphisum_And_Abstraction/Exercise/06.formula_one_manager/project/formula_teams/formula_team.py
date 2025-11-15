from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    BUDGET_NEEDED = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < self.BUDGET_NEEDED:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def sponsors(self) -> dict[str, dict[int, float]]:
        pass

    @property
    @abstractmethod
    def expenses(self) -> float:
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for sponsor in self.sponsors.values():
            for position, money in sponsor.items():
                if race_pos <= position:
                    revenue += money
                    break

        revenue -= self.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

