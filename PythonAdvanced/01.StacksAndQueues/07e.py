from collections import deque

def increase_time(time_):
    hours, minutes, sec = [int(num) for num in time_.split(":")]
    if sec== 59:
        sec = 0
        if minutes == 59:
            minutes = 0
            hours+=1
            if hours == 24:
                hours = 0
        else:
            minutes+=1
    else:
        sec +=1


    hours = str(hours).zfill(2)
    minutes = str(minutes).zfill(2)
    sec = str(sec).zfill(2)
    return f"{hours}:{minutes}:{sec}"

robots_raw = input().split(";")
robots = []
for r in robots_raw:
    name, proc = r.split("-")
    robots.append([name, int(proc), 0])

time = input()

products = deque()
while (product:=input()) != "End":
    products.append(product)

while products:
    time = increase_time(time)

    for i in range(len(robots)):
        if robots[i][2] > 0:
            robots[i][2]-=1

    taken = False
    for i in range(len(robots)):
        robot, process, time_left = robots[i]
        if time_left == 0:
            product = products.popleft()
            print(f"{robot} - {product} [{time}]")
            robots[i][2] = process
            taken = True
            break
    if not taken:
        products.rotate(-1)




