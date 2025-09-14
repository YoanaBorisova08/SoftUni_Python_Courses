from collections import deque

cups = deque(int(x) for x in input().split())
bottles = [int(x) for x in input().split()]

wasted_water = 0
while cups and bottles:
    curr_cup = cups.popleft()
    while curr_cup > 0:
        curr_bottle = bottles.pop()
        curr_cup -= curr_bottle
        if curr_cup < 0:
            wasted_water -= curr_cup

if not cups:
    print(f"Bottles:", *bottles)
else:
    print(f"Cups:", *cups)

print(f"Wasted litters of water: {wasted_water}")
