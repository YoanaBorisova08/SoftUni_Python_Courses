with open('text.txt') as file:
    MARKS = ['-', ',', '.', '!', '?']
    for row, line in enumerate(file):
        if row % 2 == 0:
            for ch in MARKS:
                line = line.replace(ch, '@')
            reversed_line = " ".join(reversed(line.split()))
            print(reversed_line)

