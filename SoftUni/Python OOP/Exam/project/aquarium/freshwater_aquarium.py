from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super().__init__(name, 50)

    def add_fish(self, fish_object):
        amount_fish = len(self.fish)
        if amount_fish >= self.capacity:
            return 'Not enough capacity.'
        if fish_object.__class__.__name__ == 'FreshwaterFish':
            self.fish.append(fish_object)
            self.capacity += 1
            return f'Successfully added FreshwaterFish to {self.name}.'
        return f'Water not suitable.'
