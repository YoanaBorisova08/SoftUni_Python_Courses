from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity:float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass

class Car(Vehicle):
    AC_CONSUMPTION = 0.9

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    AC_CONSUMPTION = 1.6
    FUEL_CONSUMPTION = 0.95

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AC_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.FUEL_CONSUMPTION

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
