from collections import deque

water_quantity = int(input())
people = deque()
while (name:=input())!="Start":
    people.append(name)
while (command:=input())!="End":
    command = command.split()
    if command[0]=="refill":
        water_quantity += int(command[1])
    else:
        liters = int(command[0])
        if liters <= water_quantity:
            print(f"{people.popleft()} got water")
            water_quantity -= liters
        else:
            print(f"{people.popleft()} must wait")
print(f"{water_quantity} liters left")
