
n = int(input())
students = {}

for i in range(n):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    avg = sum(grades)/len(grades)
    print(f"{student} -> {' '.join([f'{el:.2f}' for el in grades])} (avg: {avg:.2f})")
