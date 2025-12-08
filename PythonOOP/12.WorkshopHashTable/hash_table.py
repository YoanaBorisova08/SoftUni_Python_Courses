from typing import NamedTuple, Any

from urllib3.exceptions import NotOpenSSLWarning


class Pair(NamedTuple):
    key: Any
    value: Any

class Deleted:
    pass

class HashTable:
    DELETED = Deleted()

    def __init__(self, capacity=4):
        self.capacity = capacity
        self._array: list[Pair | Deleted | None] = [None] * self.capacity

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value<1:
            raise ValueError("Capacity must be a positive number")
        self.__capacity = value

    @property
    def array(self):
        return {pair for pair in self._array if pair not in (None, self.DELETED)}

    @property
    def _keys(self):
        return {pair.key for pair in self._array}

    @property
    def _values(self):
        return [pair.value for pair in self._array]

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def hash(self, key):
        return hash(key) % self.capacity

    def __setitem__(self, key, value):
        for index, pair in self._linear_probing(key):
            if pair is self.DELETED:
                continue
            if pair is None or pair.key == key:
                self._array[index] = Pair(key, value)
                break
        else:
            self._resize()
            self[key] = value


    def __getitem__(self, key):
        for _, pair in self._linear_probing(key):
            if pair is None:
                raise KeyError(key)
            if pair is self.DELETED:
                continue
            if pair.key == key:
                return pair.value
        else:
            raise KeyError(key)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def add(self, key, value):
        self[key] = value

    def pop(self, key, default=None):
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError:
            if default is not None:
                return default
            else:
                raise KeyError(key)

    def __len__(self):
        return len(self.array)

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __iter__(self):
        yield from self._keys

    def __delitem__(self, key):
        for index, pair in self._linear_probing(key):
            if pair is None:
              raise KeyError(key)
            if pair is self.DELETED:
                continue
            if pair.key==key:
                self._array[index] = self.DELETED
                break
        else:
            raise KeyError(key)

    def __str__(self):
        pairs = []
        for key, value in self.array:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"

    def _linear_probing(self, key):
        index = self.hash(key)
        for _ in range(0, self.capacity):
            yield index, self._array[index]
            index = (index + 1) % self.capacity

    def _resize(self):
        copy = HashTable(self.capacity*2)
        for key, value in self.array:
            copy[key] = value
        self.capacity = copy.capacity
        self._array = copy._array



