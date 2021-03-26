from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Bird(Animal):
    @abstractmethod
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"






