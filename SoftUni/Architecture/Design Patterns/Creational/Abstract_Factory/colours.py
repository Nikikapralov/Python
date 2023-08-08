from abc import ABC, abstractmethod


class AbstractColour(ABC):

    @abstractmethod
    def colour(self):
        pass


class Red(AbstractColour):

    def colour(self):
        return "Red"

class Blue(AbstractColour):

    def colour(self):
        return "Blue"