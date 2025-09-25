presents = int(input())
n = int(input())
houses = [[char for char in input().split()] for _ in range(n)]
santa_r, santa_c = next(
    ([r, c] for r, row in enumerate(houses)
     for c, col in enumerate(row) if houses[r][c]=="S"),
    None
)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

nice_kids_count = sum([row.count("V") for row in houses])
while (direction:=input()) != "Christmas morning":
    houses[santa_r][santa_c] = "-"
    dr, dc = directions[direction]
    santa_r+=dr
    santa_c+=dc

    if houses[santa_r][santa_c]=="V":
        presents -= 1

    elif houses[santa_r][santa_c]=="C":
        for dirs in directions.values():
            if houses[santa_r+dirs[0]][santa_c+dirs[1]] not in ["-", "S"]:
                presents -= 1
                houses[santa_r + dirs[0]][santa_c + dirs[1]] = "-"
                if presents==0:
                    break

    houses[santa_r][santa_c] = "S"
    if presents == 0:
        break

nice_kids_left = sum([row.count("V") for row in houses])
if nice_kids_left>0 and presents==0:
    print("Santa ran out of presents!")
[print(*row) for row in houses]
if nice_kids_left==0:
    print(f"Good job, Santa! {nice_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")
