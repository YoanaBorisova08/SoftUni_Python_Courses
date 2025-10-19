directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())
matrix = []
space_coords = ()
resources = 100

for i in range(n):
    row = input().split()
    matrix.append(row)
    for j in range(n):
        if matrix[i][j] == "S":
            space_coords = (i,j)
            matrix[space_coords[0]][space_coords[1]] = "."

while resources >= 5:
    command = input()
    resources -= 5
    if command not in directions:
        break

    new_r, new_c = space_coords[0]+directions[command][0], space_coords[1]+directions[command][1]
    if not 0<=new_r<n or not 0<=new_c<n:
        matrix[space_coords[0]][space_coords[1]] = "S"
        print("Mission failed! The spaceship was lost in space.")
        break

    if matrix[new_r][new_c] == "R":
        resources += 10
        if resources >100:
            resources = 100
    elif matrix[new_r][new_c] == "M":
        resources -= 5
        matrix[new_r][new_c] = "."
    elif matrix[new_r][new_c] == "P":
        print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        break

    space_coords = (new_r, new_c)

else:
    matrix[space_coords[0]][space_coords[1]] = "S"
    print("Mission failed! The spaceship was stranded in space.")

[print(" ".join(row)) for row in matrix]
