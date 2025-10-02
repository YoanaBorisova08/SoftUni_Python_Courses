import  os

files = {}
directory = "..\\..\\"

def get_files(folder, level=1):
    if level == -1:
        return
    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            ext = os.path.splitext(f)[1]
            if ext not in files:
                files[ext] = []
            files[ext].append(element)
        else:
            get_files(f, level - 1)

get_files(directory, -2)
with open("report.txt", "w") as report:
    for ext, filenames in sorted(files.items()):
        report.write(f"{ext}\n")
        for name in sorted(filenames):
            report.write(f"- - - {name}\n")