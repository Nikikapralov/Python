class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f'Caught {pokemon.name} with health {pokemon.health}'
        else:
            return f'This pokemon is already caught'

    def release_pokemon(self, pokemon_name: str):
        for pokemon_obj in self.pokemon:
            if pokemon_obj.name == pokemon_name:
                self.pokemon.remove(pokemon_obj)
                return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'

    def trainer_data(self):
        data_1 = f'Pokemon Trainer {self.name}\n'
        data_2 = f'Pokemon count {len(self.pokemon)}\n'
        data_3 = ''
        for pokemon_obj in self.pokemon:
            data_3 += f'- {pokemon_obj.pokemon_details()}\n'
        result = data_1 + data_2 + data_3
        return result

