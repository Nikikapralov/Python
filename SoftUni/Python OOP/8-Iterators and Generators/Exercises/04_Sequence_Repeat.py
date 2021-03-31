from collections import deque

class SequenceRepeat:

    def __init__(self, sequence, number):
        self.sequence = deque(sequence)
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        while self.number > 0:
            to_return = self.sequence.popleft()
            self.sequence.append(to_return)
            self.number -= 1
            return to_return
        raise StopIteration
