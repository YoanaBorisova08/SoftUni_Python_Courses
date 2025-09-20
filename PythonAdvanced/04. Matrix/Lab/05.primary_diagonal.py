n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
sum_primary_diagonal = 0
for i in range(n):
    sum_primary_diagonal += matrix[i][i]
print(sum_primary_diagonal)
