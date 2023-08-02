import copy
from abc import ABC, abstractmethod


class AbstractPrototype(ABC):

    @classmethod
    @abstractmethod
    def clone(cls, memo):
        pass


class Prototype(AbstractPrototype):

    def __init__(self, attribute_1, attribute_2):
        self.attribute_1 = attribute_1
        self.attribute_2 = attribute_2
        self.list_1 = []
        self.dict_1 = {}

    def clone(self, memo=None):
        if memo is None:
            memo = {}

        new_attribute_1 = self.attribute_1
        new_attribute_2 = self.attribute_2
        list_1 = copy.deepcopy(self.list_1, memo)
        dict_1 = copy.deepcopy(self.dict_1, memo)
        new = self.__class__(new_attribute_1, new_attribute_2)
        new.list_1 = list_1
        new.dict_1 = dict_1
        return new
