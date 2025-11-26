from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    VALID_ZONES: dict[str, type[BaseZone]] = {
        "RoyalZone": RoyalZone,
        "PirateZone": PirateZone
    }
    VALID_BATTLESHIPS: dict[str, type[BaseBattleship]] = {
        "RoyalBattleship": RoyalBattleship,
        "PirateBattleship": PirateBattleship
    }

    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, code: str):
        if zone_type not in self.VALID_ZONES:
            raise Exception("Invalid zone type!")
        if next((z for z in self.zones if z.code == code), None):
            raise Exception("Zone already exists!")
        self.zones.append(self.VALID_ZONES[zone_type](code))
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.VALID_BATTLESHIPS:
            raise Exception("{ship_type} is an invalid type of ship!")
        self.ships.append(self.VALID_BATTLESHIPS[ship_type](name, health, hit_strength))
        return f"A new {ship_type} was successfully added."

    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):
        if zone.volume == 0:
            return f"Zone {zone.code} does not allow more participants!"
        if ship.health <= 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if str(ship) == str(zone):
            ship.is_attacking = True

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1
        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, name: str):
        ship = next((s for s in self.ships if s.name == name), None)
        if not ship:
            return "No ship with this name!"

        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {name}."

    def start_battle(self, zone: BaseZone):
        attackers = [s for s in zone.ships if s.is_attacking]
        targets = [s for s in zone.ships if not s.is_attacking]
        if not attackers or not targets:
            return "Not enough participants. The battle is canceled."

        attacker = sorted(attackers, key=lambda s: -s.hit_strength)[0]
        target = sorted(targets, key=lambda s: -s.health)[0]

        attacker.attack()
        target.take_damage(attacker)

        if target.health <= 0:
            zone.ships.remove(target)
            self.remove_battleship(target.name)
            return f"{target.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            zone.ships.remove(attacker)
            self.remove_battleship(attacker.name)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        result = []
        available_ships = [s.name for s in self.ships if s.is_available]
        result.append(f"Available Battleships: {len(available_ships)}")
        if available_ships:
            result.append(f"#{', '.join(available_ships)}#")
        result.append(f"***Zones Statistics:***\nTotal Zones: {len(self.zones)}")
        ordered_zone = sorted(self.zones, key=lambda z: z.code)
        for zone in ordered_zone:
            result.append(zone.zone_info())
        return "\n".join(result)


