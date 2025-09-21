field_size = int(input())
commands = input().split()
field = [input().split() for _ in range(field_size)]
curr_pos = next(
    ([r, c] for r, row in enumerate(field) for c, val in enumerate(row) if val == "s"),
    None
)
coal_count = sum(row.count("c") for row in field)

for command in commands:
    x, y = curr_pos
    if command == "left":
        if 0 <= y-1:
            y-=1
        else:
            continue
    elif command == "right":
        if y+1 < field_size:
            y += 1
        else:
            continue
    elif command == "up":
        if 0 <= x - 1:
            x -= 1
        else:
            continue
    elif command == "down":
        if x+1 < field_size:
            x += 1
        else:
            continue

    if field[x][y] == "c":
        field[x][y] = "*"
        coal_count -= 1
        if coal_count == 0:
            print(f"You collected all coal! ({x}, {y})")
            break
    elif field[x][y] == "e":
        print(f"Game over! ({x}, {y})")
        break

    curr_pos = (x, y)

else:
    print(f"{coal_count} pieces of coal left. ({x}, {y})")

