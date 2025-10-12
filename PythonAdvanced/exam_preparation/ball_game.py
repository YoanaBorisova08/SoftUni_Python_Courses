from collections import deque

strength = [int(x) for x in input().split()]
accuracy = deque(int(x) for x in input().split())
goals = 0

while strength and accuracy:
    curr_strength = strength[-1]
    curr_accuracy = accuracy[0]
    curr_sum = curr_strength + curr_accuracy
    if curr_sum==100:
        goals+=1
        strength.pop()
        accuracy.popleft()
    elif curr_sum<100:
        if curr_strength < curr_accuracy:
            strength.pop()
        elif curr_strength > curr_accuracy:
            accuracy.popleft()
        else:
            strength.pop()
            accuracy.popleft()
            strength.append(curr_sum)
    else:
        strength[-1]-=10
        accuracy.rotate(-1)

if goals == 3:
    print("Paul scored a hat-trick!")
elif goals == 0:
    print("Paul failed to score a single goal.")
elif goals>3:
    print("Paul performed remarkably well!")
else:
    print("Paul failed to make a hat-trick.")

if goals>0:
    print(f"Goals scored: {goals}")

if strength:
    print(f"Strength values left: {', '.join(str(x) for x in strength)}")
if accuracy:
    print(f"Accuracy values left: {', '.join(str(x) for x in accuracy)}")
