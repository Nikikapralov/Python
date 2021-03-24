from project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, *args):
        super().__init__(*args)