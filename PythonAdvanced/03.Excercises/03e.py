from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_milk = deque([int(x) for x in input().split(', ')])
milkshakes = 0

while chocolates and cups_milk:
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_milk[0] <= 0:
        cups_milk.popleft()
        continue

    if chocolates[-1] == cups_milk[0]:
        cups_milk.popleft()
        chocolates.pop()
        milkshakes += 1

        if milkshakes == 5:
            break
    else:
        cups_milk.rotate(-1)
        chocolates[-1] -= 5
        if chocolates and chocolates[-1] <= 0:
            chocolates.pop()


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: {', '.join(map(str, cups_milk))}")
else:
    print("Milk: empty")

