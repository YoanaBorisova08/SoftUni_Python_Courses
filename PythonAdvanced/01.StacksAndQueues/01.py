expression = input()
open_brackets = []
for i in range(len(expression)):
    if expression[i] == '(':
        open_brackets.append(i)
    elif expression[i] == ')':
        start_idx = open_brackets.pop()
        end_index = i+1
        print(expression[start_idx:end_index])