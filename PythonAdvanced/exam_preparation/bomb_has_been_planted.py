time = 0
TIME_LIMIT = 16
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
rows, cols = [int(x) for x in input().split(", ")]
map_layout = []

curr_pos = None
for index in range(rows):
    data = list(input())
    if "C" in data:
        curr_pos = (index, data.index("C"))
    map_layout.append(data)



while time<TIME_LIMIT:

    direction = input()

    if direction == "defuse":
        if map_layout[curr_pos[0]][curr_pos[1]] == "B":
            time+=4
            if time<=TIME_LIMIT:
                map_layout[curr_pos[0]][curr_pos[1]] = "D"
                print("Counter-terrorist wins!")
                print(f"Bomb has been defused: {TIME_LIMIT - time} second/s remaining.")
                break
            else:
                map_layout[curr_pos[0]][curr_pos[1]] = "X"
                print("Terrorists win!")
                print("Bomb was not defused successfully!")
                print(f"Time needed: {time-TIME_LIMIT} second/s.")
                break
        else:
            time+=2
            continue
    dr=curr_pos[0]+directions[direction][0]
    dc=curr_pos[1]+directions[direction][1]
    if not(0<=dr<rows and 0<=dc<cols):
        time+=1
        continue

    if map_layout[dr][dc] == "T":
        map_layout[dr][dc] = "*"
        print("Terrorists win!")
        break
    curr_pos = (dr, dc)
    time+=1

else:
    print("Terrorists win!")
    print("Bomb was not defused successfully!")
    print(f"Time needed: 0 second/s.")

for row in map_layout:
    print("".join(row))


