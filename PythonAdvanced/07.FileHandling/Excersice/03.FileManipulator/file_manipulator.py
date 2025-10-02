import os

while(command:=input()) != "End":
    command = command.split("-")
    action, file_name = command[0], command[1]

    if action == "Create":
        open(file_name, 'w').close()

    elif action=="Add":
        content = command[2]
        with open(file_name, 'a') as file:
            file.write(content + "\n")

    elif action=="Replace":
        old_string, new_string = command[2], command[3]
        try:
            with open(file_name, 'r+') as file:
                text = file.read()
                file.seek(0)
                file.truncate(0)
                file.write(text.replace(old_string, new_string))
        except FileNotFoundError:
            print("An error occurred")

    elif action=="Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")
