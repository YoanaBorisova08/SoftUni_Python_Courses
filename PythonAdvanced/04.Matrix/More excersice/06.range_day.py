n = 5
shotgun_range = [[char for char in input().split()] for _ in range(n)]
my_r, my_c = next(
    ([r, c] for r, row in enumerate(shotgun_range)
     for c, col in enumerate(row) if shotgun_range[r][c]=="A"),
    None
)

targets_count = sum(row.count("x") for row in shotgun_range)
targets_left = targets_count
targets_hit = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}
n_commands = int(input())

for _ in range(n_commands):
    command = input().split()
    action, direction = command[0], command[1]
    dr, dc = directions[direction]

    if action == "move":
        steps = int(command[2])
        row = my_r + dr * steps
        col = my_c + dc * steps
        if 0 <= row < n and 0 <= col < n and shotgun_range[row][col] == ".":
            my_r, my_c = row, col

    elif action == "shoot":
        r, c = my_r + dr, my_c + dc
        while 0<=r<n and 0<=c<n:
            if shotgun_range[r][c]=="x":
                shotgun_range[r][c]="."
                targets_left-=1
                targets_hit.append([r, c])
                break
            r+=dr
            c+=dc
        if targets_left == 0:
            break

if targets_left == 0:
        print(f"Training completed! All {targets_count} targets hit.")
else:
    print(f"Training not completed! {targets_left} targets left.")

for target in targets_hit:
    print(target)
