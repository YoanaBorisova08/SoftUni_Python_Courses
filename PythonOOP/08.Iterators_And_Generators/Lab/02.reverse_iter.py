class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current = len(iterable)

    def __iter__(self):
        return reversed(self.iterable)


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
