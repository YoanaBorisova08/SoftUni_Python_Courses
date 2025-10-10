from lecture_modules.fibonacci_sequence.core import create_sequence, locate

sequence = None

while (command:=input()) != "Stop":
    num = int(command.split()[-1])
    if command.startswith("Create"):
        sequence = create_sequence(num)
        print(*sequence)
    else:
        if sequence:
            print(locate(num, sequence))
        else:
            print("No sequence created yet.")
