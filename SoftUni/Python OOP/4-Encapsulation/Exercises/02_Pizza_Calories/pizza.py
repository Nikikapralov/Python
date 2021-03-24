class Pizza:

    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}

    def check_capacity(self):
        capacity = self.__toppings_capacity
        toppings = len(self.__toppings)
        if capacity > toppings:
            return True
        else:
            return False

    def check_if_already_in(self, topping):
        if topping.topping_type in self.__toppings.keys():
            return True
        else:
            return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, dough):
        self.__dough = dough

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, toppings_capacity):
        self.__toppings_capacity = toppings_capacity

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        self.__toppings = value

    def add_topping(self, topping):
        if self.check_if_already_in(topping):
            self.__toppings[topping.topping_type] += topping.weight
            return
        if not self.check_capacity():
            raise ValueError('Not enough space for another topping')
        self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        total_weight = sum(self.toppings.values()) + self.dough.weight
        return total_weight
