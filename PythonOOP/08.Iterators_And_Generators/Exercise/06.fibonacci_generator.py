def fibonacci():
    curr_number = 0
    next_number = 1
    while True:
        yield curr_number
        curr_number, next_number = next_number, curr_number + next_number

generator = fibonacci()
for i in range(5):
    print(next(generator))
generator = fibonacci()
for i in range(1):
    print(next(generator))
