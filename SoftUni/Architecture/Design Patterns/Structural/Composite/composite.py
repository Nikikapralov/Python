from abc import ABC, abstractmethod


class CompositeInterface(ABC):

    def __init__(self, name=None):
        self.parent = None
        self.name = name

    # Can provide getters and setters for the parent with custom implementation.

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass

    @abstractmethod
    def is_container(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    def __repr__(self):
        return self.name

