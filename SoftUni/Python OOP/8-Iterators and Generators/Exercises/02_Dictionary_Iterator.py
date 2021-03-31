class DictionaryIter:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.value = self.dictionary.values()
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.dictionary:
            for key, value in self.dictionary.items():
                taple = (key, value)
                self.dictionary.pop(key)
                return taple
        raise StopIteration




