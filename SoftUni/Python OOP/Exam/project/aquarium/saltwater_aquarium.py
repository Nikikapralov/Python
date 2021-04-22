from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super().__init__(name, 25)

    def add_fish(self, fish_object):
        amount_fish = len(self.fish)
        if amount_fish >= self.capacity:
            return 'Not enough capacity.'
        if fish_object.__class__.__name__ == 'SaltwaterFish':
            self.fish.append(fish_object)
            self.capacity += 1
            return f'Successfully added {fish_object.__class__.__name__} to {self.name}.'
        return f'Water not suitable.'
