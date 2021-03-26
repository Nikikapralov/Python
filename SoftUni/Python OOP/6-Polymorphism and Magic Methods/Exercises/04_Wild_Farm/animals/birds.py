from project.animals.animal import Bird
from project.food import Meat
from project.food import Seed
from project.food import Vegetable
from project.food import Fruit


class Owl(Bird):
    def __init__(self, *args):
        super().__init__(*args)

    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food):
        if not isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    def __init__(self, *args):
        super().__init__(*args)

    def make_sound(self):
        return 'Cluck'

    def feed(self, food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity


