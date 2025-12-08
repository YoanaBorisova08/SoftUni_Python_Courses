from unittest import TestCase, main

from hash_table import HashTable, Pair


class TestHashTable(TestCase):
    def setUp(self):
        self.hashtable = HashTable(4)
        self.hashtable._array = [Pair(0, 0), Pair(1, 1), Pair(2, 2), Pair(3, 3)]

    def test_set_item(self):
        del self.hashtable[1]
        self.hashtable[5] = 5
        print(self.hashtable)
        self.assertEqual("{0: 0, 5: 5, 2: 2, 3: 3", str(self.hashtable))

if __name__ == "__main__":
    main()