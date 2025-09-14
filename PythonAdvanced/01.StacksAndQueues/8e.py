from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
passed_count = 0
car_crash = False
while (line:=input()) != "END":
    if line == "green":
        green_left = green_light

        while green_left > 0 and cars:
            curr_car = cars.popleft()
            green_left -= len(curr_car)
            if 0 <= green_left or -green_left <= free_window:
                passed_count += 1
                continue
            green_left +=free_window
            print(f"A crash happened!")
            print(f"{curr_car} was hit at {curr_car[green_left]}.")
            car_crash = True
            break

    else:
        cars.append(line)

    if car_crash:
        break

if not car_crash:
    print("Everyone is safe.")
    print(f"{passed_count} total cars passed the crossroads.")
