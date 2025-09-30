import os
from files.constants import path_to_dir

path = os.path.join(path_to_dir, "files", "numbers.txt")
file = open(path, 'r')
numbers = [int(el) for el in file.read().split("\n") if el]
print(sum(numbers))