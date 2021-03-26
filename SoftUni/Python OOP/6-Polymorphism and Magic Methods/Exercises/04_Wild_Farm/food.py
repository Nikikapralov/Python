from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, *args):
        super().__init__(*args)


class Fruit(Food):
    def __init__(self, *args):
        super().__init__(*args)


class Meat(Food):
    def __init__(self, *args):
        super().__init__(*args)


class Seed(Food):
    def __init__(self, *args):
        super().__init__(*args)

