class Appliance:
    def __init__(self, cost):
        self.cost = float(cost)

    def get_monthly_expense(self):
        monthly_cost = self.cost * 30
        return monthly_cost

