from composite import CompositeInterface


class Leaf(CompositeInterface):

    def __init__(self, price, name="Leaf"):
        super().__init__(name=name)
        self.price = price

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def is_container(self):
        return False

    def execute(self):
        return [self.price]
