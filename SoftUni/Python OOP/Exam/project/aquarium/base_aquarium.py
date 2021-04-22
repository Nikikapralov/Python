from abc import abstractmethod, ABC


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, names, capacity):
        self.name = names
        self.capacity = int(capacity)
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Aquarium name cannot be an empty string.')
        self.__name = value

    def calculate_comfort(self):
        total = 0
        for decoration in self.decorations:
            total += decoration.comfort
        return total

    def add_fish(self, fish_object):
        pass

    def remove_fish(self, fish_object):
        if fish_object in self.fish:
            self.fish.remove(fish_object)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for obj in self.fish:
            obj.eat()

    def __str__(self):
        if not self.fish:
            fish_names = 'none'
        else:
            fish_names = ' '.join([obj.name for obj in self.fish])
        result = f'{self.name}:\n' \
                 f'Fish: {fish_names}\n' \
                 f'Decorations: {len(self.decorations)}\n' \
                 f'Comfort: {self.calculate_comfort()}'
        return result






