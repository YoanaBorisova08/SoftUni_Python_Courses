from collections import deque

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

bees = deque([int(n) for n in input().split()])
nectar = [int(n) for n in input().split()]
operations = deque(input().split())
honey = 0

while bees and nectar:
    while nectar and bees[0] > nectar[-1]:
        nectar.pop()
    if not nectar:
        break

    if operations[0] == "/" and nectar[-1] == 0:
        bees.popleft()
        nectar.pop()
        operations.popleft()
    else:
        honey += abs(operators[operations.popleft()](bees.popleft(), nectar.pop()))

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
