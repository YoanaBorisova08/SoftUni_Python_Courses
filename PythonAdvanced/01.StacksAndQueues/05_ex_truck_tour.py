from collections import deque

n = int(input())
petrol_pumps = deque()

for _ in range(n):
    petrol, distance = input().split()
    petrol_pumps.append([int(petrol), int(distance)])

start = 0

while start < n:
    finished_circle = True
    curr_petrol = 0
    for petrol, distance in petrol_pumps:
        curr_petrol += petrol
        if curr_petrol >= distance:
            curr_petrol -= distance
        else:
            finished_circle = False
            start+=1
            petrol_pumps.rotate(-1)
            break
    if finished_circle:
        break

print(start)

