from project.mammal import Mammal

from unittest import TestCase, main
class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test name", "Test type", "Test sound")

    def test_init(self):
        self.assertEqual("Test name", self.mammal.name)
        self.assertEqual("Test type", self.mammal.type)
        self.assertEqual("Test sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Test name makes Test sound", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual("Test name is of type Test type", result)

if __name__ == "__main__":
    main()