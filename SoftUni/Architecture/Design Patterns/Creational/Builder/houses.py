from abc import ABC, abstractmethod


class AbstractHouse(ABC):
    def __init__(self):
        self.house_parts = []

    @abstractmethod
    def check_available_to_live(self):
        pass


class NormalHouse(AbstractHouse):

    def check_available_to_live(self):
        for item in ["walls", "doors", "windows"]:
            if item not in self.house_parts:
                return "Not liveable"
        return "Available to live"


class Mansion(AbstractHouse):
    def check_available_to_live(self):
        for item in ["walls", "doors", "windows", "pool", "shed", "garden"]:
            if item not in self.house_parts:
                return "Not liveable"
        return "Available to live"

