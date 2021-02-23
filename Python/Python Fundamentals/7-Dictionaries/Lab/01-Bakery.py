class Stock:
    def __init__(self, ingredients):
        self.ingredients = ingredients.split()
        self.dict_ingredients = {}
        self.key = None
        self.value = None

    def key_or_value(self):
        for index, value in enumerate(self.ingredients):
            if index % 2 == 0:
                self.key = value
            else:
                self.value = int(value)
            self.add_to_dict(self.key, self.value)

    def add_to_dict(self, key, value):
        self.dict_ingredients.update({key: value})

    def print_dict(self):
        return self.dict_ingredients


stock_1 = Stock(input())
stock_1.key_or_value()
print(stock_1.print_dict())



