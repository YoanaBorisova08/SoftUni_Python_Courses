from collections import deque
potions = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90: "Draught of Wisdom",
    80: "Potion of Agility",
    70: "Elixir of Strength",
}

substances = [int(x) for x in input().split(", ")]
crystals = deque([int(x) for x in input().split(", ")])
crafted_potions = []

while substances and crystals and len(crafted_potions)<5:
    curr_substance = substances.pop()
    curr_crystal = crystals.popleft()
    mix = curr_substance + curr_crystal

    if mix in potions and potions[mix] not in crafted_potions:
        crafted_potions.append(potions[mix])

    else:
        for potion in potions.keys():
            if mix > potion and potions[potion] not in crafted_potions:
                crafted_potions.append(potions[potion])
                if curr_crystal-20>0:
                    crystals.append(curr_crystal-20)
                break
        else:
            if curr_crystal-5>0:
                crystals.append(curr_crystal-5)

if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")
if substances:
    reversed_substances = substances[::-1]
    print(f"Substances: {', '.join(map(str, reversed_substances))}")
if crystals:
    print(
        f"Crystals: {', '.join(map(str, crystals))}")
