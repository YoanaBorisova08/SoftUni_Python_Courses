
def fill_the_box(h, l, w, *args):
    volume = h*l*w
    cubes = 0
    for cube in args:
        if cube=="Finish":
            break
        cubes+=cube
    if volume>cubes:
        return f"There is free space in the box. You could put {volume-cubes} more cubes."
    return f"No more free space! You have {cubes-volume} more cubes."



print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
