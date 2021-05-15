class ArrayList:

    def __init__(self, size=4, main_list=None, items=0):
        self.size = size
        self.items = items
        self.main_list = [None] * self.size
        if main_list is not None:
            for index, value in enumerate(main_list):
                self.main_list[index] = value

    def __iter__(self, value):
        for item in self.main_list:
            if item is not None:
                yield item
            return

    def __getitem__(self, item):
        return self.main_list[item]

    def __str__(self):
        return str(self.__get_repr())

    def __add__(self, iterable):
        if hasattr(iterable, '__iter__'):
            for item in iterable:
                self.__array_append(item)
            return ArrayList(self.size, self.main_list, self.items)
        else:
            raise ValueError

    def __len__(self):
        return len(self.__get_repr())

    def append(self, value):
        self.__array_append(value)
        return self.__str__()

    def remove(self, index):
        if index in range(0, self.items):
            to_return = self.main_list[index]
            for item in range(index, self.items):
                self.main_list[item] = self.main_list[item + 1]
            self.items -= 1
        else:
            raise IndexError
        return to_return

    def extend(self, iterable):
        return self.__add__(iterable)

    def get(self, index):
        return self.__getitem__(index)

    def insert(self, index, value):
        if self.size == self.items:
            self.__grow_list()
        for item in range(self.items - 1, index - 1, -1):
            self.main_list[item + 1] = self.main_list[item]
        self.main_list[index] = value
        self.items += 1
        return self.__str__()

    def pop(self):
        value = self.main_list[self.items - 1]
        self.main_list[self.items - 1] = None
        return value

    def clear(self):
        self.main_list = [None] * self.size

    def index(self, value):
        for index, item in enumerate(self.main_list):
            if item == value:
                return index
        raise ValueError

    def count(self, value):
        counter = 0
        for item in self.main_list:
            if item == value:
                counter += 1
        return counter

    def reverse(self):
        return self.__get_repr()[::-1]

    def copy(self):
        return ArrayList(self.size, self.main_list, self.items)

    def add_first(self, value):
        self.insert(0, value)

    def dictionize(self):
        my_list = self.__get_repr()
        keys = [item for index, item in enumerate(my_list) if index % 2 == 0]
        values = [item for index, item in enumerate(my_list) if index % 2 == 1]
        if values < keys:
            values.append(' ')
        zipped = zip(keys, values)
        result = {}
        for key, value in zipped:
            result[key] = value
        return result

    def move(self, amount):
        if amount > self.items:
            raise ValueError
        elif amount == self.items:
            return self.__get_repr()
        index = amount - 1
        to_move = []
        for item in range(0, index + 1):
            to_move.append(self.main_list[item])
        for item in range(index + 1, self.items):
            self.main_list[item - amount] = self.main_list[item]
            self.main_list[item] = 'None'
        self.items -= amount
        for item in to_move:
            self.__array_append(item)
        return self.__get_repr()

    def sum(self):
        total_sum = 0
        for value in self.__get_repr():
            if not isinstance(value, (int, float)):
                total_sum += len(value)
            else:
                total_sum += value
        return total_sum

    def overbound(self):
        dictionary = {}
        for index, entry in enumerate(self.__get_repr()):
            if not isinstance(entry, (int, float)):
                value = len(entry)
            else:
                value = entry
            dictionary[index] = value

        biggest = sorted(dictionary.items(), key=lambda x: -x[1])[0][0]
        return biggest

    def underbound(self):
        dictionary = {}
        for index, entry in enumerate(self.__get_repr()):
            if not isinstance(entry, (int, float)):
                value = len(entry)
            else:
                value = entry
            dictionary[index] = value

        smallest = sorted(dictionary.items(), key=lambda x: x[1])[0][0]
        return smallest

    def __get_repr(self):
        return [item for item in self.main_list if item is not None]

    def __grow_list(self):
        self.main_list += [None] * self.size
        self.size *= 2

    def __array_append(self, value):
        if self.items == self.size:
            self.__grow_list()
        self.main_list[self.items] = value
        self.items += 1
