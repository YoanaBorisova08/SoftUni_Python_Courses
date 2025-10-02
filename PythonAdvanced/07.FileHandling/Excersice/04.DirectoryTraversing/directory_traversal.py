import  os

files = {}
directory = "..\\"

for element in os.listdir(directory):
    f = os.path.join(directory, element)
    if os.path.isfile(f):
        ext = os.path.splitext(f)[1]
        if ext not in files:
            files[ext] = []
        files[ext].append(element)
    else:
        for el in os.listdir(f):
            filename = os.path.join(f, el)
            if os.path.isfile(filename):
                ext = os.path.splitext(filename)[1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)

with open("report.txt", "w") as report:
    for ext, filenames in sorted(files.items()):
        report.write(f"{ext}\n")
        for name in sorted(filenames):
            report.write(f"- - - {name}\n")

