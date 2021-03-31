class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index <= -1:
            raise StopIteration()
        return self.iterable[self.index]

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
