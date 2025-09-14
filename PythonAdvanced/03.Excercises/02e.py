from collections import deque
expression = deque(input().split())
numbers = deque()

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
}

for curr_el in expression:
    if curr_el in operators.keys():
        result = numbers.popleft()
        while numbers:
            result = operators[curr_el](result, numbers.popleft())
        numbers.append(result)
    else:
        numbers.append(int(curr_el))

print(result)
