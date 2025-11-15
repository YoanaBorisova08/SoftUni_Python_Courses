from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit

class Mouse(Mammal):
    @property
    def weight_increment(self):
        return 0.10

    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    @staticmethod
    def make_sound():
        return "Squeak"

class Dog(Mammal):
    @property
    def weight_increment(self):
        return 0.40

    @property
    def allowed_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "Woof!"

class Cat(Mammal):
    @property
    def weight_increment(self):
        return 0.30

    @property
    def allowed_food(self):
        return [Vegetable, Meat]

    @staticmethod
    def make_sound():
        return "Meow"

class Tiger(Mammal):
    @property
    def weight_increment(self):
        return 1.00

    @property
    def allowed_food(self):
        return [Meat]

    @staticmethod
    def make_sound():
        return "ROAR!!!"
