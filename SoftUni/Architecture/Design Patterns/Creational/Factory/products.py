from abc import ABC, abstractmethod


class ProductInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def do_stuff(self):
        pass


class ProductA(ProductInterface):
    def do_stuff(self):
        return 'Product A'


class ProductB(ProductInterface):
    def do_stuff(self):
        return 'Product B'
