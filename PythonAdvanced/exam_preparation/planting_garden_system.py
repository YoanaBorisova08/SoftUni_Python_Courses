
def plant_garden(free_space: float, *plants, **plant_requests):
    plants_types = {}
    for plant, place in plants:
        plants_types[plant] = place

    sorted_requests = sorted(plant_requests.items(), key=lambda x: x[0])
    planted = {}
    all_planted = True
    not_origin = 0
    for request, quantity in sorted_requests:
        if request in plants_types.keys() and free_space >= plants_types[request]:
            required_space = plants_types[request] * quantity
            if free_space >= required_space:
                free_space -= required_space
                planted[request] = quantity
            else:
                all_planted = False
                quantity_fit = int(free_space // plants_types[request])
                free_space -= plants_types[request] * quantity_fit
                planted[request] = quantity_fit
        else:
            not_origin+=1
        if free_space <= 0:
            break

    result = ""
    if all_planted and len(planted) == len(plant_requests) - not_origin:
        result+= f"All plants were planted! Available garden space: {free_space:.1f} sq meters.\n"
    else:
        result+= f"Not enough space to plant all requested plants!\n"
    result+=f"Planted plants:\n"
    for request, quantity in planted.items():
        if quantity > 0:
            result+=f"{request}: {quantity}\n"
    return result



print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))