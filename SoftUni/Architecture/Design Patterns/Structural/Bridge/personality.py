from abc import ABC, abstractmethod


class AbstractPersonality(ABC):

    @abstractmethod
    def show_emotion(self):
        pass


class EvilPersonality(AbstractPersonality):

    def show_emotion(self):
        return "I laugh when people suffer "


class GoodPersonality(AbstractPersonality):

    def show_emotion(self):
        return "I show empathy when people suffer "

