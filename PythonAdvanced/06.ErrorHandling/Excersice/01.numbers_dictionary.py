
numbers_dictionary = {}

while (line:=input()) != "Search":
    number_as_string = line
    try:
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
    else:
        numbers_dictionary[number_as_string] = number

while (line:=input()) != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

while (line:=input()) != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

print(numbers_dictionary)
