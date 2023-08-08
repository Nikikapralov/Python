from abc import ABC, abstractmethod


class AbstractButton(ABC):
    def __init__(self, colour):
        self.colour = colour

    @abstractmethod
    def click(self):
        pass


class WindowsButton(AbstractButton):

    def click(self):
        return f"Windows {self.colour.colour()} click."


class MacOSButton(AbstractButton):

    def click(self):
        return f"MacOS {self.colour.colour()} click."