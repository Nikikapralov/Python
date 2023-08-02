from abc import ABC, abstractmethod


class CharacterClass(ABC):

    @abstractmethod
    def use_skill(self):
        pass


class Mage(CharacterClass):

    def __init__(self, personality):
        self.personality = personality

    def use_skill(self):
        return self.personality.show_emotion() + "Fireball"


class Barbarian(CharacterClass):

    def __init__(self, personality):
        self.personality = personality

    def use_skill(self):
        return self.personality.show_emotion() + "Hammer smash"

