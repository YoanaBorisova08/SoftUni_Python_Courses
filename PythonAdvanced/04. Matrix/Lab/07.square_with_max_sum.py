rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(num) for num in input().split(", ")] for _ in range(rows)]
max_sum = float("-inf")
max_matrix = None
for i in range(1, rows):
    for j in range(1, cols):
        curr_matrix = [[matrix[i-1][j-1], matrix[i-1][j]], [matrix[i][j-1], matrix[i][j]]]
        curr_sum = sum(el for row in curr_matrix for el in row)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_matrix = curr_matrix

print(*max_matrix[0])
print(*max_matrix[1])
print(max_sum)
