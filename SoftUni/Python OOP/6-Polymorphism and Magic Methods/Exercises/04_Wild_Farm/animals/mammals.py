from project.animals.animal import Mammal
from project.food import Meat
from project.food import Seed
from project.food import Vegetable
from project.food import Fruit


class Mouse(Mammal):
    def __init__(self, *args):
        super().__init__(*args)

    def make_sound(self):
        return 'Squeak'

    def feed(self, food):
        if not isinstance(food, Vegetable) and isinstance(food, Fruit):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, *args):
        super().__init__(*args)

    def make_sound(self):
        return 'Woof!'

    def feed(self, food):
        if not isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self, *args):
        super().__init__(*args)

    def make_sound(self):
        return 'Meow'

    def feed(self, food):
        if not isinstance(food, Vegetable) and isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self, *args):
        super().__init__(*args)

    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food):
        if not isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += 1.00 * food.quantity
        self.food_eaten += food.quantity
