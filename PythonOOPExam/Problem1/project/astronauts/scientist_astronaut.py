from project.astronauts.base_astronaut import BaseAstronaut


class ScientistAstronaut(BaseAstronaut):
    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, "ScientistAstronaut", 70)

    @property
    def increase_stamina(self):
        return 3