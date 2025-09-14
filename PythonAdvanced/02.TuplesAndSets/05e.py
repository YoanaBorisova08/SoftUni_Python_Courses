
n = int(input())
longest_intersection = set()
for _ in range(n):
    parts = input().split('-')
    first_start, first_end = map(int, parts[0].split(','))
    second_start, second_end = map(int, parts[1].split(','))
    first_set = set()
    second_set = set()
    for i in range(first_start, first_end+1):
        first_set.add(int(i))
    for i in range(second_start, second_end+1):
        second_set.add(int(i))
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] \
with length {len(longest_intersection)}")
