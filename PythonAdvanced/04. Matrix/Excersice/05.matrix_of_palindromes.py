rows, cols = [int(x) for x in input().split()]
a_ord = 97
matrix = [[f"{chr(a_ord+i)}{chr(a_ord+i+j)}{chr(a_ord+i)}" for j in range(cols)] for i in range(rows)]
[print(*matrix[i]) for i in range(rows)]