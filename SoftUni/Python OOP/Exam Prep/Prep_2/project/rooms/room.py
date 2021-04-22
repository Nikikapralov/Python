class Room:
    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = float(budget)
        self.members_count = members_count
        self.children = []
        self.__expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self.__expenses = value

    @staticmethod
    def calculate_expenses(*args):
        total = 0
        for el in args:
            for item in el:
                total += item.cost
        return total







