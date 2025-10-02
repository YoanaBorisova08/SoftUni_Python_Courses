from collections import deque
rows, cols = [int(x) for x in input().split()]
snake = deque(input())
matrix = []
for r in range(rows):
    matrix.append([])
    for c in range(cols):
        matrix[r].append(snake[0])
        snake.rotate(-1)
    if r%2==1:
        matrix[r].reverse()
[print(*row, sep="") for row in matrix]
