class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


car = Car("a", "b", 1, 4)
#car.make = ""
print(car)


from unittest import TestCase, main
class CarManagerTests(TestCase):
    def test_init(self):
        car = Car("Toyota", "Corolla", 6.5, 50)
        self.assertEqual("Toyota", car.make)
        self.assertEqual("Corolla", car.model)
        self.assertEqual(6.5, car.fuel_consumption)
        self.assertEqual(50, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

        car.fuel_amount = 20
        self.assertEqual(20, car.fuel_amount)

    def test_make_empty_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car(None, "ModelX", 5, 50)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car("", "ModelX", 5, 50)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_modul_empty_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Tesla", "", 5, 50)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car("Tesla", None, 5, 50)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Tesla", "ModelX", 0, 50)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car("Tesla", "ModelX", -5, 50)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_zero_or_negative_raises(self):
        with self.assertRaises(Exception) as ex:
            car = Car("Tesla", "ModelX", 5, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car = Car("Tesla", "ModelX", 5, -50)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_negative_raises(self):
        car = Car("Tesla", "ModelX", 5, 50)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -10
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))
        self.assertEqual(0, car.fuel_amount)

    def test_refuel_zero_or_negative_raises(self):
        car = Car("Tesla", "ModelX", 5, 50)
        with self.assertRaises(Exception) as ex:
            car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.assertEqual(0, car.fuel_amount)

    def test_refuel_within_capacity(self):
        c = Car("Tesla", "ModelX", 5, 50)
        c.fuel_amount = 20
        c.refuel(20)
        self.assertEqual(40, c.fuel_amount)

    def test_refuel_exceeding_capacity(self):
        c = Car("Tesla", "ModelX", 5, 50)
        c.fuel_amount = 40
        c.refuel(20)
        self.assertEqual(50, c.fuel_amount)

    def test_drive_not_enough_fuel_raises(self):
        c = Car("Tesla", "ModelX", 5, 50)
        c.fuel_amount = 10
        with self.assertRaises(Exception) as ex:
            c.drive(300)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.assertEqual(10, c.fuel_amount)

    def test_drive_reduces_fuel_amount(self):
        c = Car("Tesla", "ModelX", 5, 50)
        c.fuel_amount = 20
        c.drive(100)
        self.assertEqual(15, c.fuel_amount)
        c.drive(200)
        self.assertEqual(5, c.fuel_amount)

    def test_drive_exact_fuel_amount(self):
        c = Car("Tesla", "ModelX", 5, 50)
        c.fuel_amount = 10
        c.drive(200)
        self.assertEqual(0, c.fuel_amount)



if __name__ == '__main__':
    main()

