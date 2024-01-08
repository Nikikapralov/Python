from collections.abc import Iterator, Iterable


class ForwardIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
        except IndexError:
            raise StopIteration
        self._position += 1
        return value


class ReverseIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._position = -1

    def __next__(self):
        try:
            value = self._collection[self._position]
        except IndexError:
            raise StopIteration
        self._position -= 1
        return value


class WordsCollection(Iterable):
    def __init__(self, words, default_iterator=ForwardIterator):
        self._words = words
        self.default_iterator = default_iterator

    def __iter__(self):
        return self.default_iterator(self._words)

    def iterate(self, iterator):
        return iterator(self._words)



