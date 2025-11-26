from project.furniture import Furniture
from unittest import TestCase, main

class FurnitureTests(TestCase):
    model = "Test model"
    price = 2.5
    dimensions = (1, 1, 1)
    in_stock = True
    weight = 1.3
    def setUp(self):
        self.test_furniture = Furniture(
            self.model,
            self.price,
            self.dimensions,
            self.in_stock,
            self.weight
        )

    def test_init(self):
        self.assertEqual(self.model, self.test_furniture.model)
        self.assertEqual(self.price, self.test_furniture.price)
        self.assertEqual(self.dimensions, self.test_furniture.dimensions)
        self.assertEqual(self.in_stock, self.test_furniture.in_stock)
        self.assertEqual(self.weight, self.test_furniture.weight)

    def test_model_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.test_furniture.model = ""
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.test_furniture.model = "A" * 51
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(ex.exception))

    def test_model_setter_success(self):
        new_model = "New Model"
        self.test_furniture.model = new_model
        self.assertEqual(new_model, self.test_furniture.model)

    def test_price_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.test_furniture.price = -1.0
        self.assertEqual("Price must be a non-negative number.", str(ex.exception))

    def test_price_setter_success(self):
        new_price = 10.0
        self.test_furniture.price = new_price
        self.assertEqual(new_price, self.test_furniture.price)

    def test_dimensions_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.test_furniture.dimensions = (1, 2)
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.test_furniture.dimensions = (1, -2, 3)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.test_furniture.dimensions = (0, 2, 3)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))

    def test_dimensions_setter_success(self):
        new_dimensions = (2, 3, 4)
        self.test_furniture.dimensions = new_dimensions
        self.assertEqual(new_dimensions, self.test_furniture.dimensions)

    def test_weight_setter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.test_furniture.weight = -1.0
        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.test_furniture.weight = 0.0
        self.assertEqual("Weight must be greater than zero.", str(ex.exception))


    def test_weight_setter_success(self):
        new_weight = 5.0
        self.test_furniture.weight = new_weight
        self.assertEqual(new_weight, self.test_furniture.weight)

    def test_get_available_status_in_stock(self):
        expected = f"Model: {self.model} is currently in stock."
        self.assertEqual(expected, self.test_furniture.get_available_status())

    def test_get_available_status_out_of_stock(self):
        self.test_furniture.in_stock = False
        expected = f"Model: {self.model} is currently unavailable."
        self.assertEqual(expected, self.test_furniture.get_available_status())

    def test_get_specifications(self):
        expected = (f"Model: {self.model} has the following dimensions: "
                f"{1}mm x {1}mm x {1}mm and weighs: {self.weight}")
        self.assertEqual(expected, self.test_furniture.get_specifications())

        self.test_furniture.weight = None
        expected = (f"Model: {self.model} has the following dimensions: "
                    f"{1}mm x {1}mm x {1}mm and weighs: N/A")
        self.assertEqual(expected, self.test_furniture.get_specifications())


if __name__ == '__main__':
    main()
