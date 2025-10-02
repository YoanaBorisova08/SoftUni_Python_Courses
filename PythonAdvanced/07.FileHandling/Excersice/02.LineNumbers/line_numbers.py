
with open('text.txt') as file, open("output.txt", 'w') as output_file:
    result = []
    for row, line in enumerate(file):
        letters_count = 0
        punctuation_count = 0
        for ch in line:
            if ch.isalpha():
                letters_count += 1
            elif not ch.isspace():
                punctuation_count += 1
        result.append(f"Line {row+1}: {line[:-1]} ({letters_count})({punctuation_count})")

    output_file.write("\n".join(result))
