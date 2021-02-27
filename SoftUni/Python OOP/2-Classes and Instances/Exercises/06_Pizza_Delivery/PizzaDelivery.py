class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = float(price)
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, ingredient_price):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
        else:
            self.ingredients[ingredient] += quantity

        self.price += ingredient_price * quantity

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
        elif ingredient in self.ingredients:
            amount_we_have = self.ingredients[ingredient]
            if amount_we_have < quantity:
                return f'Please check again the desired quantity of {ingredient}!'
            else:
                self.ingredients[ingredient] -= quantity
            self.price -= ingredient_price * quantity

    def make_order(self):
        PizzaDelivery.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join([f'{key}: {value}' for key, value in self.ingredients.items()])} and the price will be {self.price}lv."


