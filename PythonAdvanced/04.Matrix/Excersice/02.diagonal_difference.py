n = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(n)]
primary_diagonal = [matrix[i][i] for i in range(n)]
sec_diagonal = [matrix[i][n - 1 - i] for i in range(n)]
diff = abs(sum(primary_diagonal) - sum(sec_diagonal))
print(diff)
