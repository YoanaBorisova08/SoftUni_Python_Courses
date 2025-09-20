rows, cols = [int(x) for x in input().split()]
matrix = [[char for char in input().split()] for _ in range(rows)]
count_squares = 0
for r in range(1, rows):
    for c in range(1, cols):
        if matrix[r-1][c-1] == matrix[r-1][c] == matrix[r][c-1] == matrix[r][c]:
            count_squares+=1
print(count_squares)
