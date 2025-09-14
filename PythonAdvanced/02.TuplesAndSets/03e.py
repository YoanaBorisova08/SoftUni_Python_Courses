
n = int(input())
ch_elements = set()
for _ in range(n):
    elements = input().split()
    for el in elements:
        ch_elements.add(el)

for el in ch_elements:
    print(el)
