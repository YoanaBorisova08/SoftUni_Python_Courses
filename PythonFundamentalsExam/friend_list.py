def valid_index(idx: int, lentgh: int) -> bool:
    return 0<= idx < lentgh

friends = input().split(', ')
while (command:=input()) != "Report":
    command = command.split()
    action = command[0]
    match action:
        case 'Blacklist':
            name = command[1]
            if name in friends:
                friends[friends.index(name)] = 'Blacklisted'
                print(f"{name} was blacklisted.")
            else:
                print(f"{name} was not found.")
        case 'Error':
            index = int(command[1])
            if valid_index(index, len(friends)) and \
                    friends[index]!='Blacklisted' and friends[index]!='Lost':
                print(f"{friends[index]} was lost due to an error.")
                friends[index] = 'Lost'
        case 'Change':
            index = int(command[1])
            new_name = command[2]
            if valid_index(index, len(friends)):
                print(f"{friends[index]} changed his username to {new_name}.")
                friends[index] = new_name

else:
    print(f"Blacklisted names: {sum(1 for name in friends if name=='Blacklisted')}")
    print(f"Lost names: {sum(1 for name in friends if name=='Lost')}")
    print(' '.join(friends))