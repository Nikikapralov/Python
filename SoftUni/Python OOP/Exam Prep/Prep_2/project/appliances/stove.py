from project.appliances.appliance import Appliance


class Stove(Appliance):
    def __init__(self):
        super().__init__(0.7)

    def __rmul__(self, other):
        while other > 0:
            other -= 1
            yield Stove()