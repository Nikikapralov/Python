import copy


class SomeClass:
    def __init__(self, attribute_1, attribute_2):
        self.attribute_1 = attribute_1
        self.attribute_2 = attribute_2
        self.dict = {}
        self.list = {}

    def __copy__(self):
        """
        Creates a shallow copy. Be careful with lists and dictionaries.
        """
        attr_1 = self.attribute_1
        attr_2 = self.attribute_2
        dict_1 = copy.copy(self.dict)
        list_1 = copy.copy(self.list)
        new = self.__class__(attr_1, attr_2)
        new.dict = dict_1
        new.list = list_1

        return new

    def __deepcopy__(self, memodict=None):

        if memodict is None:
            memodict = {}

        attr_1 = self.attribute_1
        attr_2 = self.attribute_2
        dict_1 = copy.deepcopy(self.dict, memodict)
        list_1 = copy.deepcopy(self.list, memodict)
        new = self.__class__(attr_1, attr_2)
        new.dict = dict_1
        new.list = list_1

        return new

