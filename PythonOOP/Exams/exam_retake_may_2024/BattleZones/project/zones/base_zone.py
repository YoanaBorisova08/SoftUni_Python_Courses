from abc import ABC, abstractmethod

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: list[BaseBattleship] = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if not value.isdigit():
            raise ValueError( "Zone code must contain digits only!")
        self.__code = value

    @abstractmethod
    def __str__(self):
        pass

    def get_ships(self):
        return sorted(self.ships, key=lambda s: (-s.hit_strength, s.name))

    def zone_info(self):
        zone_type = str(self)
        enemy_type = "Royal" if zone_type == "Pirate" else "Pirate"
        enemy_ships_count = sum(1 for ship in self.ships if ship.__str__== enemy_type)
        result = (f"@{zone_type} Zone Statistics@\n"
                f"Code: {self.code}; Volume: {self.volume}\n"
                f"Battleships currently in the {zone_type} Zone: {len(self.ships)}, {enemy_ships_count} out of them are {enemy_type} Battleships.")
        if self.ships:
            result+=f"\n#{', '.join(s.name for s in self.get_ships())}#"
        return result

