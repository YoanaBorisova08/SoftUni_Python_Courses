n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
while (command:=input()) != "END":
    command = command.split()
    action = command[0]
    row, col, value = [int(x) for x in command[1:]]
    if not (0<=row<n and 0<=col<n):
        print("Invalid coordinates")
    else:
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value

[print(*row) for row in matrix]
