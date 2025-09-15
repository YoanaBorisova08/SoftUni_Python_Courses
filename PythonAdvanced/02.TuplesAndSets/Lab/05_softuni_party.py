
n = int(input())
guests = set()
for _ in range(n):
    guests.add(input())
while (guest:=input()) != "END":
    if guest in guests:
        guests.remove(guest)
print(len(guests))
sorted_guests = sorted(guests)
for guest in sorted_guests:
    print(guest)
