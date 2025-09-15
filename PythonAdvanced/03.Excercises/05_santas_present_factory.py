from collections import deque
toys = {
    300: ["Teddy bear", 0],
    400: ["Bicycle", 0],
    150: ["Doll", 0],
    250: ["Wooden train", 0],

}

boxes = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
success = False

while boxes and magic_levels:
    magic = boxes[-1]*magic_levels[0]

    if magic in toys.keys():
        toys[magic][1]+=1
        boxes.pop()
        magic_levels.popleft()

        if (toys[150][1] >=1 and toys[250][1] >=1) \
                or (toys[300][1] >=1 and toys[400][1] >=1):
            success = True
    else:
        if magic<0:
            boxes.append(boxes.pop()+magic_levels.popleft())
        elif magic>0:
            boxes[-1] += 15
            magic_levels.popleft()
        else:
            if boxes[-1] == 0:
                boxes.pop()
            if magic_levels[0] == 0:
                magic_levels.popleft()

if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    print(f"Materials left: {', '.join(map(str, boxes[::-1]))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

filtered_toys = [(name, quality) for name, quality in (info for info in toys.values()) if quality > 0]
filtered_toys.sort(key=lambda x: x[0])
for name, quality in filtered_toys:
    print(f"{name}: {quality}")
