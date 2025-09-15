chat = []
while (command:=input()) != "end":
    command = command.split()
    action = command[0]
    message = command[1]
    match action:
        case 'Chat':
            chat.append(message)
        case 'Delete':
            if message in chat:
                chat.remove(message)
        case 'Edit':
            edited_message = command[2]
            if message in chat:
                chat[chat.index(message)] = edited_message
        case 'Pin':
            if message in chat:
                chat.remove(message)
                chat.append(message)
        case 'Spam':
            for i in range(1, len(command)):
                chat.append(command[i])

else:
    for text in  chat:
        print(text)
