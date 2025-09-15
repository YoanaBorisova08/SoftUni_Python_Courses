from collections import deque

total_food_quantity = int(input())
orders = deque(int(num) for num in input().split())

print(max(orders))

while orders:
    if orders[0] <= total_food_quantity:
        total_food_quantity -= orders.popleft()
    else:
        break

if orders:
    print(f"Orders left:", *orders)
else:
    print("Orders complete")
