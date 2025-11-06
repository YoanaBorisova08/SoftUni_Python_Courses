from project.food import Food

class Fruit(Food):
    def __init__(self, name:str, date: str):
        super().__init__(date)
        self.name = name


