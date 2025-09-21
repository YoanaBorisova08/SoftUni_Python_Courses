n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
bombs =  [list(map(int, bomb.split(","))) for bomb in input().split()]

for x, y in bombs:
    if matrix[x][y] <= 0:
        continue
    power = matrix[x][y]
    for r in range(x-1, x+2):
        for c in range(y-1, y+2):
            if 0<=r<n and 0<=c<n and matrix[r][c] > 0:
                matrix[r][c]-=power
    matrix[x][y] = 0

alive_cells = [cell for row in matrix for cell in row if cell>0]
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]
