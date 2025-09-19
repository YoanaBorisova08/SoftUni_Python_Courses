n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))

symbol = input()
position = None

for i in range(n):
    for j in range(n):
        if matrix[i][j] == symbol:
            position = (i, j)
            print(f"({position[0]}, {position[1]})")
            exit()

print(f"{symbol} does not occur in the matrix")
