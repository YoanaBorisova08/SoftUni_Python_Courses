
class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: dict = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill: str, mana_cost: float):
        if skill in self.skills:
            return "Skill already added"
        self.skills[skill] = mana_cost
        return f"Skill {skill} added to the collection of the player {self.name}"

    def player_info(self):
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        for skill, mana in self.skills.items():
            result+=f"==={skill} - {mana}\n"
        return result
