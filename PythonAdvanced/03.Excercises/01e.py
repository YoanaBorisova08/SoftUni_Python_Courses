
first_set = set(int(num) for num in input().split())
second_set = set(int(num) for num in input().split())
n = int(input())

for _ in range(n):
    command, name, *numbers = input().split()
    numbers = [int(x) for x in numbers]

    if command == "Add":
        if name == "First":
            for num in numbers:
                first_set.add(int(num))
        else:
            for num in numbers:
                second_set.add(int(num))

    elif command == "Remove":
        if name == "First":
            for num in numbers:
                if num in first_set:
                    first_set.remove(int(num))
        else:
            for num in numbers:
                if num in second_set:
                    second_set.remove(int(num))

    elif command == "Check":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

sorted_first_set = sorted(first_set)
sorted_second_set = sorted(second_set)
print(*sorted_first_set, sep = ", ")
print(*sorted_second_set, sep = ", ")
