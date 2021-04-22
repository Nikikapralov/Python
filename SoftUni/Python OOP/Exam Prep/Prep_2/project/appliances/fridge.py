from project.appliances.appliance import Appliance


class Fridge(Appliance):
    def __init__(self):
        super().__init__(1.2)

    def __rmul__(self, other):
        while other > 0:
            other -= 1
            yield Fridge()

