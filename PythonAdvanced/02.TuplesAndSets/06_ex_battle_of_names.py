
n = int(input())
odd_results = set()
even_results = set()

for row in range(1, n+1):
    name = input()
    sum_letters = 0
    for char in name:
        sum_letters += ord(char)
    result = sum_letters // row
    if result % 2 == 1:
        odd_results.add(result)
    else:
        even_results.add(result)

odd_value = sum(odd_results)
even_value = sum(even_results)

if odd_value == even_value:
    print(*odd_results.union(even_results), sep=", ")
elif odd_value > even_value:
    print(*odd_results.difference(even_results), sep=", ")
else:
    print(*even_results.symmetric_difference(odd_results), sep=", ")
