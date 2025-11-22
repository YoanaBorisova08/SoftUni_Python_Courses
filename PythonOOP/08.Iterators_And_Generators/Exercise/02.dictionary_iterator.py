class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dict_tuple = tuple(dictionary.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.dict_tuple):
            return self.dict_tuple[self.index]
        raise StopIteration

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
