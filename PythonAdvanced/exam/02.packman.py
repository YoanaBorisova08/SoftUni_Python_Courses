directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

initial_health = 100
n = int(input())
matrix = []
pacman = ()
stars_left = 0

for i in range(n):
    matrix.append([x for x in input()])
    for j in range(n):
        if matrix[i][j] == "P":
            pacman = (i, j)
            matrix[i][j] = "-"
        elif matrix[i][j] == "*":
            stars_left += 1

while (command:=input())!= "end":
    curr_r = pacman[0] + directions[command][0]
    curr_c = pacman[1] + directions[command][1]
    if not 0<=curr_r<n:
        curr_r = (n-1) if curr_r<0 else 0
    if not 0<=curr_c<n:
        curr_c = (n-1) if curr_c<0 else 0

    if matrix[curr_r][curr_c] == "*":
        stars_left -= 1
        matrix[curr_r][curr_c] = "-"
        if stars_left == 0:
            print("Pacman wins! All the stars are collected.")
            pacman = (curr_r, curr_c)
            break

    elif matrix[curr_r][curr_c] == "G":
        initial_health -= 50
        matrix[curr_r][curr_c] = "-"
        if initial_health <= 0:
            print(f"Game over! Pacman last coordinates [{curr_r},{curr_c}]")
            pacman = (curr_r, curr_c)
            break

    elif matrix[curr_r][curr_c] == "F":
        initial_health += 50
        matrix[curr_r][curr_c] = "-"

    pacman = (curr_r, curr_c)
else:
    print("Pacman failed to collect all the stars.")

matrix[pacman[0]][pacman[1]] = "P"
print(f"Health: {initial_health}")
if stars_left:
    print(f"Uncollected stars: {stars_left}")

[print("".join(row)) for row in matrix]

