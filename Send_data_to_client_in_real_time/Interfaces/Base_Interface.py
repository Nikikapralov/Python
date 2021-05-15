from abc import ABC, abstractmethod

"""Template for the Interface classes. Each interface (presence, io, vehicle_image) should have its own class,
which must inherit BaseInterface."""


class BaseInterface(ABC):
    RAW_DATA = None

    @abstractmethod
    def __init__(self, json_data=None):
        self.json_data = json_data

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    def create(cls, value):
        return cls(value)

