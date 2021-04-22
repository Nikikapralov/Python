from project.appliances.appliance import Appliance


class Laptop(Appliance):
    def __init__(self):
        super().__init__(1)

    def __rmul__(self, other):
        while other > 0:
            other -= 1
            yield Laptop()