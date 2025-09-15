
expression = input()
open_parenthesis = []
matching_brackets = {
    "(": ")",
    "{": "}",
    "[":"]"
}
balanced =True
for char in expression:
    if char in "([{":
        open_parenthesis.append(char)
    elif open_parenthesis:
        if char != matching_brackets[open_parenthesis.pop()]:
            balanced = False
            break
    else:
        balanced = False
        break
else:
    if open_parenthesis:
        balanced = False

print("YES" if balanced else "NO")