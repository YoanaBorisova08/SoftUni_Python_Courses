from unittest import TestCase, main
from custom_list import CustomList

class CustomListTest(TestCase):
    def setUp(self):
        self.customList = CustomList(100, 2, -15, 2)
    def test_init(self):
        cl = CustomList(1, 2, 3)
        self.assertEqual([1, 2, 3], cl._CustomList__data)

    def test_add(self):
        self.assertEqual([100, 2, -15, 2], self.customList._CustomList__data)
        result = self.customList.append(5)
        self.assertEqual([100, 2, -15, 2, 5], result)

    def test_get_elements(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())

    def test_remove(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.remove(1)
        self.assertEqual([100, -15, 2], self.customList.get_elements())
        self.assertEqual(2, result)

    def test_get(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.get(1)
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        self.assertEqual(2, result)

    def test_extend(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.extend([8, 9, 10, 11])
        self.assertEqual([100, 2, -15, 2, 8, 9, 10, 11], self.customList.get_elements())
        self.assertEqual([100, 2, -15, 2, 8, 9, 10, 11], result)

    def test_insert(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.insert(2, 15)
        self.assertEqual([100, 2, 15, -15, 2], self.customList.get_elements())
        self.assertEqual([100, 2, 15, -15, 2], result)

    def test_pop(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.pop()
        self.assertEqual([100, 2, -15], self.customList.get_elements())
        self.assertEqual(2, result)

    def test_clear(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.clear()
        self.assertEqual([], self.customList.get_elements())
        self.assertEqual([], self.customList._CustomList__data)
        self.assertIsNone(result)

    def test_index(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.index(2)
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        self.assertEqual(1, result)

    def test_count(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.count(2)
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        self.assertEqual(2, result)

    def test_reverse(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.reverse()
        self.assertEqual([2, -15, 2, 100], result)
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())

    def test_copy(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.copy()
        self.assertEqual([100, 2, -15, 2], result)
        self.assertNotEqual(id(self.customList.get_elements()), id(result))

    def test_size(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.size()
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        self.assertEqual(4, result)

    def test_add_first(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.add_first(3)
        self.assertEqual([3, 100, 2, -15, 2], self.customList.get_elements())
        self.assertIsNone(result)

    def test_dictionize(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.dictionize()
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        self.assertEqual({100:2, -15: 2}, result)

        self.customList.insert(2, -5)
        self.assertEqual([100, 2, -5, -15, 2], self.customList.get_elements())
        result = self.customList.dictionize()
        self.assertEqual([100, 2, -5, -15, 2], self.customList.get_elements())
        self.assertEqual({100:2, -5:-15, 2:" " }, result)

    def test_move(self):
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        result = self.customList.move(2)
        self.assertEqual([100, 2, -15, 2], self.customList.get_elements())
        self.assertEqual([-15, 2, 100, 2], result)

    def test_sum(self):
        cl = CustomList(1, [1, 2], "asd", 100)
        result = cl.sum()
        self.assertEqual(106, result)

    def test_overbound(self):
        cl = CustomList(1, "asd", [1, 2])
        result = cl.overbound()
        self.assertEqual(1, result)

    def test_underbound(self):
        cl = CustomList(1, "asd", [1, 2])
        result = cl.underbound()
        self.assertEqual(0, result)

if __name__ == '__main__':
    main()
