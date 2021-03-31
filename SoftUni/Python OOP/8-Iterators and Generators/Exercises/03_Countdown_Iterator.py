class CountdownIterator:

    def __init__(self, count):
        self.count = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count -= 1
        if 0 > self.count:
            raise StopIteration
        return self.count
