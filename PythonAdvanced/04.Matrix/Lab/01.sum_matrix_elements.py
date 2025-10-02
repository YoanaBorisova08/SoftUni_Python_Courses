rows, cols = [int(x) for x in input().split(", ")]
matrix = []
sum_elements = 0
for r in range(rows):
    data = [int(x) for x in input().split(", ")]
    matrix.append(data)
    sum_elements += sum(data)
print(sum_elements)
print(matrix)
