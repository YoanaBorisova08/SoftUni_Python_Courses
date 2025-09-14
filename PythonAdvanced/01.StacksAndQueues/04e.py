
clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_rack_left = rack_capacity
number_of_racks = 1
while clothes:
    current_clothes = clothes.pop()
    if current_rack_left >= current_clothes:
        current_rack_left -= current_clothes
    else:
        number_of_racks += 1
        current_rack_left = rack_capacity - current_clothes
print(number_of_racks)