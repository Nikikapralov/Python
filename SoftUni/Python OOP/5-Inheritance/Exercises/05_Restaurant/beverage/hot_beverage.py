from project.beverage.beverage import Beverage


class HotBeverage(Beverage):
    def __init__(self, *args):
        super().__init__(*args)