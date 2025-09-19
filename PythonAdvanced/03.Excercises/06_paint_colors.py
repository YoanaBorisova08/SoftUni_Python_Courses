from collections import deque

substrings = deque(input().split())
main_colors = ["red", "yellow", "blue"]
sec_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"],
}
made_colors = []

while substrings:
    first_str = substrings.popleft()
    last_str = substrings.pop() if substrings else ""
    for color in (first_str + last_str, last_str + first_str):
        if color in main_colors or color in sec_colors.keys():
            made_colors.append(color)
            break
    else:
        first_part = first_str[:-1] if first_str else ""
        second_part = last_str[:-1] if last_str else ""
        middle = len(substrings) // 2
        if first_part:
            substrings.insert(middle, first_part)
        if second_part:
            substrings.insert(middle, second_part)

final_colors = []
for color in made_colors:
    if color in sec_colors.keys():
        if all(main in made_colors for main in sec_colors[color]):
           final_colors.append(color)
    else:
        final_colors.append(color)

print(final_colors)
