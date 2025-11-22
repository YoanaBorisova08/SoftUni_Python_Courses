class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < self.number:
            return self.sequence[self.i%len(self.sequence)]
        raise StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
