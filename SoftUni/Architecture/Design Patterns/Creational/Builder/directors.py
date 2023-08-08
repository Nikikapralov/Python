from abc import ABC, abstractmethod

class AbstractDirector(ABC):
    def __init__(self, builder):
        self.builder = builder

    @abstractmethod
    def construct_normal_house(self):
        pass

    @abstractmethod
    def construct_mansion(self):
        pass


class HousingDirector(AbstractDirector):
    """
    Should not be normal house and mansion, should instead have a different director for each
    and have create barebones and create luxurious, where the functions will be naturally
    different depending on the Mansion or House inheritance.
    """

    def construct_normal_house(self):
        self.builder.build_doors().build_walls().build_windows()
        return self.builder.built_object

    def construct_mansion(self):
        self.builder.build_doors().build_walls().build_windows().build_pool().build_shed().build_garden()
        return self.builder.built_object