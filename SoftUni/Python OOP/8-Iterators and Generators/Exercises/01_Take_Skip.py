class TakeSkip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.number = - self.step

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.current:
            raise StopIteration
        self.current += 1
        self.number += self.step
        return self.number

