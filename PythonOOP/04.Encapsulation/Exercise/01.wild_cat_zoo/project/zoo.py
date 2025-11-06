from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list = []
        self.workers: list = []

    def add_animal(self, animal, price: float):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, name):
        for worker in self.workers:
            if worker.name == name:
                self.workers.remove(worker)
                return f"{name} fired successfully"
        return f"There is no {name} in the zoo"

    def pay_workers(self):
        sums = 0
        for worker in self.workers:
            sums+=worker.salary
        if sums <= self.__budget:
            self.__budget -= sums
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money = 0
        for animal in self.animals:
            money+=animal.money_for_care
        if money <= self.__budget:
            self.__budget -= money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: float):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if isinstance(animal, Lion):
                lions.append(animal)
            elif isinstance(animal, Tiger):
                tigers.append(animal)
            elif isinstance(animal, Cheetah):
                cheetahs.append(animal)
        result = [f"You have {len(self.animals)} animals"]
        result.append(f"----- {len(lions)} Lions:")
        for lion in lions:
            result.append(f"{repr(lion)}")
        result.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            result.append(f"{repr(tiger)}")
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah in cheetahs:
            result.append(f"{repr(cheetah)}")
        return "\n".join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        keeper = []
        caretaker = []
        vet = []
        for worker in self.workers:
            if isinstance(worker, Caretaker):
                caretaker.append(worker)
            elif isinstance(worker, Keeper):
                keeper.append(worker)
            elif isinstance(worker, Vet):
                vet.append(worker)
        result.append(f'----- {len(keeper)} Keepers:')
        for k in keeper:
            result.append(f"{repr(k)}")
        result.append(f'----- {len(caretaker)} Caretakers:')
        for c in caretaker:
            result.append(f"{repr(c)}")
        result.append(f'----- {len(vet)} Vets:')
        for v in vet:
            result.append(f"{repr(v)}")
        return "\n".join(result)







