class Child:
    def __init__(self, food_cost, *toys_cost):
        self.toys_cost = toys_cost
        self.food_cost = food_cost
        self.cost = float(self.food_cost + sum(toys_cost))