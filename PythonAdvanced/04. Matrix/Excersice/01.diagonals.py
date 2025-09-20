n = int(input())
matrix = [[int(num) for num in input().split(", ")] for _ in range(n)]
primary_diagonal = [matrix[i][i] for i in range(n)]
sec_diagonal = [matrix[i][n - 1 - i] for i in range(n)]
print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in sec_diagonal])}. Sum: {sum(sec_diagonal)}")