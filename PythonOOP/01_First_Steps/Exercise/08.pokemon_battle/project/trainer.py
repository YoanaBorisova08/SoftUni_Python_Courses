from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons: list[Pokemon] = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, p):
        for pokemon in self.pokemons:
            if p == pokemon.name:
                self.pokemons.remove(pokemon)
                return f"You have released {p}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for p in self.pokemons:
            result+=f"- {p.pokemon_details()}\n"
        return result
