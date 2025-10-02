n = int(input())
field = [[char for char in input().split()] for _ in range(n)]
bunny_r, bunny_c = next(
    ([r, c] for r, row in enumerate(field)
    for c, col in enumerate(row) if field[r][c] == "B"),
    None
)
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

best_direction = None
best_path = []
max_eggs = float("-inf")

for direction, (dr, dc) in directions.items():
    path = []
    eggs = 0
    r, c = bunny_r + dr, bunny_c + dc

    while 0<=r<n and 0<=c<n and field[r][c]!="X":
        eggs += int(field[r][c])
        path.append([r, c])
        r+=dr
        c+=dc

    if eggs>max_eggs and path:
        best_direction = direction
        best_path = path
        max_eggs = eggs

print(best_direction)
for path in best_path:
    print(path)
print(max_eggs)
