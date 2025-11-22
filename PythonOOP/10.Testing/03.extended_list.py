class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

from unittest import TestCase, main


class IntegerListTests(TestCase):
    def setUp(self):
        self.integerList = IntegerList(100, 1, 20)

    def test_init(self):
        i = IntegerList(1, "5", 10.7, 6)
        self.assertEqual([1, 6], i.get_data())
        self.assertEqual([1, 6], i._IntegerList__data)

    def test_add_not_int_raises(self):
        self.assertEqual([100, 1, 20], self.integerList.get_data())

        with self.assertRaises(ValueError) as ex:
            self.integerList.add("5")
            self.assertEqual(["Element is not Integer"], str(ex.exception))

        self.assertEqual([100, 1, 20], self.integerList.get_data())

        with self.assertRaises(ValueError) as ex:
            self.integerList.add([])
            self.assertEqual(["Element is not Integer"], str(ex.exception))

        self.assertEqual([100, 1, 20], self.integerList.get_data())

        with self.assertRaises(ValueError) as ex:
            self.integerList.add(6.8)
            self.assertEqual(["Element is not Integer"], str(ex.exception))

        self.assertEqual([100, 1, 20], self.integerList.get_data())

    def test_add(self):
        self.assertEqual([100, 1, 20], self.integerList.get_data())

        result = self.integerList.add(100)

        self.assertEqual([100, 1, 20, 100], self.integerList.get_data())
        self.assertEqual([100, 1, 20, 100], result)

    def test_remove_index_not_valid_idx_raises(self):
        self.assertEqual([100, 1, 20], self.integerList.get_data())

        with self.assertRaises(IndexError) as ex:
            self.integerList.remove_index(4)
            self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual([100, 1, 20], self.integerList.get_data())

    def test_remove_index(self):
        self.assertEqual([100, 1, 20], self.integerList.get_data())

        result = self.integerList.remove_index(1)
        self.assertEqual([100, 20], self.integerList.get_data())
        self.assertEqual(1, result)

    def test_get_invalid_index_raises(self):
        self.assertEqual([100, 1, 20], self.integerList.get_data())

        with self.assertRaises(IndexError) as ex:
            self.integerList.get(3)
            self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual([100, 1, 20], self.integerList.get_data())

    def test_get(self):
        self.assertEqual([100, 1, 20], self.integerList.get_data())
        result = self.integerList.get(0)
        self.assertEqual(100, result)

    def test_insert_invalid_index_raises(self):
        self.assertEqual([100, 1, 20], self.integerList.get_data())

        with self.assertRaises(IndexError) as ex:
            self.integerList.insert(100, 1)
            self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual([100, 1, 20], self.integerList.get_data())

    def test_insert_invalid_element_type_raises(self):
        self.assertEqual([100, 1, 20], self.integerList.get_data())

        with self.assertRaises(ValueError) as ex:
            self.integerList.insert(1, 100.2)
            self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual([100, 1, 20], self.integerList.get_data())

    def test_insert(self):
        self.assertEqual([100, 1, 20], self.integerList.get_data())
        self.integerList.insert(1, 50)
        self.assertEqual([100, 50, 1, 20], self.integerList.get_data())

    def test_get_biggest(self):
        self.integerList.insert(0, 30)
        self.assertEqual([30, 100, 1, 20], self.integerList.get_data())
        result = self.integerList.get_biggest()
        self.assertEqual(100, result)

    def test_get_index(self):
        self.integerList.insert(2, 20)
        self.assertEqual([100, 1, 20, 20], self.integerList.get_data())
        result = self.integerList.get_index(20)
        self.assertEqual(2, result)

if __name__ == "__main__":
    main()