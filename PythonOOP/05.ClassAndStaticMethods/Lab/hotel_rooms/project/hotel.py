from project.room import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: list[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def status(self):
        self.guests = sum(r.guests for r in self.rooms if r.is_taken)
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\nTaken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}"


