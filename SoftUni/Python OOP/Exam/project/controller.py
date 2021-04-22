from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type == 'FreshwaterAquarium':
            aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == 'SaltwaterAquarium':
            aquarium = SaltwaterAquarium(aquarium_name)
        else:
            return 'Invalid aquarium type.'
        self.aquariums.append(aquarium)
        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type):
        if decoration_type == 'Ornament':
            decoration = Ornament()
        elif decoration_type == 'Plant':
            decoration = Plant()
        else:
            return 'Invalid decoration type.'
        self.decorations_repository.add(decoration)
        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name, decoration_type):
        aquarium_exists = self.__get_aquarium_by_name(aquarium_name)
        decoration_type_exists = self.decorations_repository.find_by_type(decoration_type)
        if aquarium_exists and (decoration_type_exists != 'None'):
            self.decorations_repository.remove(decoration_type_exists)
            aquarium_exists.add_decoration(decoration_type_exists)
            return f'Successfully added {decoration_type} to {aquarium_name}.'
        if decoration_type != 'Plant' and decoration_type != 'Ornament':
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        if fish_type == 'FreshwaterFish':
            fish_object = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == 'SaltwaterFish':
            fish_object = SaltwaterFish(fish_name, fish_species, price)
        else:
            return f"There isn't a fish of type {fish_type}."
        return aquarium.add_fish(fish_object)

    def feed_fish(self, aquarium_name):
        aquarium_exists = self.__get_aquarium_by_name(aquarium_name)
        aquarium_exists.feed()
        amount_fish = len(aquarium_exists.fish)
        return f'Fish fed: {amount_fish}'

    def calculate_value(self, aquarium_name):
        aquarium_exists = self.__get_aquarium_by_name(aquarium_name)
        decorations_cost = sum([dec.price for dec in aquarium_exists.decorations])
        fish_cost = sum([fish_obj.price for fish_obj in aquarium_exists.fish])
        total = decorations_cost + fish_cost
        return f'The value of Aquarium {aquarium_name} is {total:.2f}.'

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += aquarium.__str__()
            return result

    def __get_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if getattr(aquarium, 'name') == aquarium_name:
                return aquarium






