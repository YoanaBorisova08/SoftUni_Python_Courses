rows, cols = [int(x) for x in input().split()]
matrix = [[int(num) for num in input().split()] for _ in range(rows)]
max_sum = -float("inf")
max_matrix=None
for i in range(rows-2):
    for j in range(cols-2):
        curr_matrix = [
            [matrix[i][j], matrix[i][j+1], matrix[i][j+2]],
            [matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2]],
            [matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]
        ]
        curr_sum = sum(curr_matrix[0]) + sum(curr_matrix[1]) + sum(curr_matrix[2])
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_matrix = curr_matrix
print(f"Sum = {max_sum}")
[print(*row) for row in max_matrix]
