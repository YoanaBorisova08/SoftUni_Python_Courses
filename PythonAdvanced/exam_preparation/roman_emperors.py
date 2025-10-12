

def list_roman_emperors(*args, **kwargs): #(name, status) {name:rule}
    result=[]
    successful = {}
    unsuccessful = {}
    for name, status in args:
        if status:
            successful[name] = int(kwargs[name])
        else:
            unsuccessful[name] = int(kwargs[name])

    sorted_successful = sorted(successful.items(), key=lambda x: (-x[1], x[0]))
    sorted_unsuccessful = sorted(unsuccessful.items(), key=lambda x: (x[1], x[0]))

    result.append(f"Total number of emperors: {len(successful) + len(unsuccessful)}")
    if successful:
        result.append("Successful emperors:")
        for name, value in sorted_successful:
            result.append(f"****{name}: {value}")
    if unsuccessful:
        result.append("Unsuccessful emperors:")
        for name, value in sorted_unsuccessful:
            result.append(f"****{name}: {value}")

    return "\n".join(result)
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))