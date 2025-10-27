def print_spaces(spaces, stars):
    print(' ' * (spaces) + '* ' * stars)

def print_top(n):
    for i in range(1, n + 1):
        print_spaces(n - i, i)

def print_bottom(n):
    for i in range(1, n):
        print_spaces(i, n-i)

n = int(input())
print_top(n)
print_bottom(n)