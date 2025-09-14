from collections import deque
queue = deque()

while (name:=input())!="End":
    if name == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(name)

print(f"{len(queue)} people remaining.")