import os
from files.constants import path_to_dir

path = os.path.join(path_to_dir, "files", "text.txt")
try:
    file = open(path)
except FileNotFoundError:
    print("File not found")
else:
    print("File found")
    file.close()