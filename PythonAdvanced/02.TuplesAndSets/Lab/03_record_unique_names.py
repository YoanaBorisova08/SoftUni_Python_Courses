n = int(input())
cars = set()
for _ in range(n):
    data = input().split(", ")
    if data[0] == "IN":
        cars.add(data[1])
    else:
        cars.discard(data[1])

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
