
lists = input().split("|")
lists.reverse()
flatten = [int(num) for l in lists for num in l.split()]
print(*flatten)