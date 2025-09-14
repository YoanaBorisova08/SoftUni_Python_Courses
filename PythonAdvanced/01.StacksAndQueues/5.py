from collections import deque
kids = deque(input().split())
n_rotations = int(input()) - 1
while len(kids)>1:
    kids.rotate(-n_rotations)
    name = kids.popleft()
    print(f"Removed {name}")
print(f"Last is {kids[0]}")