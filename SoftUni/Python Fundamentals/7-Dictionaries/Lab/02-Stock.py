class Stock:
    def __init__(self, ingredients):
        self.ingredients = ingredients.split()
        self.dict_ingredients = {}
        self.key = None
        self.value = None
        self.wanted_product = None

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

    def is_in_stock(self, item):
        self.wanted_product = item
        if self.wanted_product in self.dict_ingredients:
            return f'We have {self.dict_ingredients[self.wanted_product]} of {self.wanted_product} left'
        else:
            return f"Sorry, we don't have {self.wanted_product}"


stock_1 = Stock(input())
stock_1.key_or_value()
wanted_products = input().split()
for item in wanted_products:
    print(stock_1.is_in_stock(item))
