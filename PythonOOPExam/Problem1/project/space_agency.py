from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []
        self.stations: list[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        VALID_ASTRONAUTS = {
            "EngineerAstronaut": EngineerAstronaut,
            "ScientistAstronaut": ScientistAstronaut
        }

        if astronaut_type not in VALID_ASTRONAUTS:
            raise ValueError("Invalid astronaut type!")

        astronaut = next((a for a in self.astronauts if a.id_number == astronaut_id_number), None)
        if astronaut:
            raise ValueError(f"{astronaut_id_number} has been already added!")

        self.astronauts.append(VALID_ASTRONAUTS[astronaut_type](astronaut_id_number, astronaut_salary))
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        VALID_STATIONS = {
            "MaintenanceStation": MaintenanceStation,
            "ResearchStation": ResearchStation
        }

        if station_type not in VALID_STATIONS:
            raise ValueError("Invalid station type!")

        station = next((s for s in self.stations if s.name == station_name), None)
        if station:
            raise ValueError(f"{station_name} has been already added!")

        self.stations.append(VALID_STATIONS[station_type](station_name))
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        station = next((s for s in self.stations if s.name == station_name), None)
        if not station:
            raise ValueError(f"Station {station_name} does not exist!")

        astronaut = next((a for a in self.astronauts if a.specialization == astronaut_type), None)
        if not astronaut:
            raise ValueError("No available astronauts of the type!")

        if station.capacity<=0:
            return "This station has no available capacity."

        self.astronauts.remove(astronaut)
        station.add_astronaut(astronaut)
        return f"{astronaut.id_number} was assigned to {station_name}."

    @staticmethod
    def train_astronauts(station: BaseStation, sessions_number: int):
        for _ in range(sessions_number):
            for astronaut in station.astronauts:
                astronaut.train()
        total_stamina = sum(astronaut.stamina for astronaut in station.astronauts)
        return f"{station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."

    @staticmethod
    def retire_astronaut(station: BaseStation, astronaut_id_number: str):
        astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)
        if not astronaut or astronaut.stamina == 100:
            return "The retirement process was canceled."

        station.remove_astronaut(astronaut)
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):
        for station in self.stations:
            station.update_salaries(min_value)

        sorted_stations = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))
        total_available_capacity = sum(station.capacity for station in self.stations)
        result = (f"*Space Agency Up-to-Date Report*\n"
                  f"Total number of available astronauts: {len(self.astronauts)}\n"
                  f"**Stations count: {len(self.stations)}; Total available capacity: {total_available_capacity}**")
        for s in sorted_stations:
            result+=f"\n{s.status()}"
        return result