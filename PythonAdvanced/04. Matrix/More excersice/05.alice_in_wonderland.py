n = int(input())
land = [[char for char in input().split()] for _ in range(n)]
alice_r, alice_c = next(
    ([r, c] for r, row in enumerate(land)
    for c, col in enumerate(row) if land[r][c] == "A"),
    None
)
land[alice_r][alice_c] = "*"

tea_bags = 0
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while tea_bags<10:
    command = input()
    alice_r += directions[command][0]
    alice_c += directions[command][1]
    if not (0<=alice_r<n and 0<=alice_c<n):
        break
    position = land[alice_r][alice_c]
    land[alice_r][alice_c] = "*"
    if position.isdigit():
        tea_bags += int(position)
    elif position == "R":
        break

if tea_bags>=10:
    print(f"She did it! She went to the party.")
else:
    print(f"Alice didn't make it to the tea party.")

[print(*row) for row in land]
