from copy import deepcopy
from sys import maxsize


class CustomList:
    def __init__(self, *args):
        self.__data = list(args)

    def append(self, el):
        self.__data.append(el)
        return self.__data

    def get_elements(self):
        return self.__data

    def remove(self, idx):
        return self.__data.pop(idx)

    def get(self, idx):
        return self.__data[idx]

    def extend(self, it):
        self.__data.extend(it)
        return self.__data

    def insert(self, idx, el):
        self.__data.insert(idx, el)
        return self.__data

    def pop(self):
        return self.__data.pop()

    def clear(self ):
        self.__data.clear()

    def index(self, value):
        return self.__data.index(value)

    def count(self, el):
        return self.__data.count(el)

    def reverse(self):
        return self.__data[::-1]

    def copy(self):
        return deepcopy(self.__data)

    def size(self):
        return len(self.__data)

    def add_first(self, value):
        self.__data.insert(0, value)

    def dictionize(self):
        data = {}
        for index in range(0, len(self.__data), 2):
            try:
                data[self.__data[index]] = self.__data[index + 1]
            except IndexError:
                data[self.__data[index]] = " "
        return data

    def move(self, count):
        first_part = self.__data[:count]
        second_part = self.__data[count:]
        return second_part+first_part

    def sum(self):
        result = 0
        for el in self.__data:
            if isinstance(el, int):
                result += el
            else:
                result += len(el)
        return result

    def overbound(self):
        max_el = -maxsize
        biggest_el_index = None
        for index in range(0, len(self.__data)):
            if isinstance(self.__data[index], int):
                element = self.__data[index]
            else:
                element = len(self.__data[index])
            if element > max_el:
                max_el = element
                biggest_el_index = index

        return biggest_el_index

    def underbound(self):
        min_el = maxsize
        smallest_el_index = None

        for index in range(0, len(self.__data)):
            if isinstance(self.__data[index], int):
                element = self.__data[index]
            else:
                element = len(self.__data[index])
            if element < min_el:
                min_el = element
                smallest_el_index = index

        return smallest_el_index