class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.end:
            raise StopIteration
        return self.current

