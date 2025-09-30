import os
from files.constants import path_to_dir

path = os.path.join("nested.txt")
try:
    file = open(path)
except FileNotFoundError:
    print("file not found")
else:
    print(file.read())
    file.close()

