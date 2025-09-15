
occurrences = {}
text = input()
for char in text:
    if char not in occurrences.keys():
        occurrences[char] = text.count(char)
occurrences = sorted(occurrences.items(), key=lambda item: item[0])
for char, occ in occurrences:
    print(f"{char}: {occ} time/s")