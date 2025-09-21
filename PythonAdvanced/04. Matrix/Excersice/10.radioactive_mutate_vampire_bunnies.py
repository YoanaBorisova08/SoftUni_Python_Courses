def multiply_bunnies(matrix, bunnies):
    length = len(bunnies)
    for idx in range(length):
        r, c = bunnies[idx]
        if 0 <= r-1: #up
            matrix[r-1][c]="B"
            bunnies.append((r-1, c))
        if r+1 < n: #down
            matrix[r+1][c]="B"
            bunnies.append((r+1, c))
        if 0 <= c-1: #left
            matrix[r][c-1]="B"
            bunnies.append((r, c-1))
        if c+1 < m: #down
            matrix[r][c+1]="B"
            bunnies.append((r, c+1))


n, m = [int(x) for x in input().split()]
lair = [[char for char in input()] for _ in range(n)]
commands = [char for char in input()]
player_pos = next(
    ([r, c] for r, row in enumerate(lair)
     for c, val in enumerate(row)
     if val == "P"),
    None
)
lair[player_pos[0]][player_pos[1]]="."
bunnies_pos = [(r, c)
          for r, row in enumerate(lair)
          for c, val in enumerate(row)
          if val == "B"]

moves = {
    "U": lambda r, c: (r-1, c),
    "D": lambda r, c: (r+1, c),
    "L": lambda r, c: (r, c-1),
    "R": lambda r, c: (r, c+1),
}

for command in commands:
    x = player_pos[0]
    y = player_pos[1]
    x, y = moves[command](x, y)
    multiply_bunnies(lair, bunnies_pos)
    if not 0 <= x < n or not 0 <= y < m:
        [print(*row, sep="") for row in lair]
        print(f"won: {player_pos[0]} {player_pos[1]}")
        break
    if lair[x][y] == "B":
        [print(*row, sep="") for row in lair]
        print(f"dead: {x} {y}")
        break
    player_pos = [x, y]

