from project.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliliters = float(milliliters)

    @property
    def milliliters(self):
        return self.__milliliters

    @milliliters.setter
    def milliliters(self, value):
        self.__milliliters = value
