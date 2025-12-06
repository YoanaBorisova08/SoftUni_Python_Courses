from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant
from project.plants.base_plant import BasePlant
from project.clients.base_client import BaseClient


class FlowerShopManager():
    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        VALID_PLANT_TYPES = {
            "Flower": Flower,
            "LeafPlant": LeafPlant
        }
        if plant_type not in VALID_PLANT_TYPES:
            raise ValueError("Unknown plant type!")
        if plant_type == "LeafPlant":
            plant_extra_data = int(plant_extra_data)
        self.plants.append(VALID_PLANT_TYPES[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data))
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        VALID_CLIENT_TYPES = {
            "RegularClient": RegularClient,
            "BusinessClient": BusinessClient
        }
        if client_type not in VALID_CLIENT_TYPES:
            raise ValueError("Unknown client type!")

        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if client is None:
            raise ValueError("This phone number has been used!")

        self.clients.append(VALID_CLIENT_TYPES[client_type](client_name, client_phone_number))
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        client = next((c for c in self.clients if c.phone_number == client_phone_number), None)
        if client is None:
            raise ValueError("Client not found!")
        plants = [p for p in self.plants if p.name == plant_name]
        if not plants:
            raise ValueError("Plants not found!")
        if len(plants) < plant_quantity:
            return "Not enough plant quantity."

        removed_plants = 0
        curr_index = 0
