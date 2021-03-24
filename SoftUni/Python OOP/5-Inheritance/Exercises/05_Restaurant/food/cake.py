from project.food.dessert import Dessert


class Cake(Dessert):
    CALORIES = 1000
    PRICE = 5
    GRAMS = 250

    def __init__(self, name):
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)