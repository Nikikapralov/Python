class Stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        to_return = f'[{", ".join([el for el in reversed(self.data)])}]'
        return to_return

    def push(self, item):
        self.data.append(item)

    def pop(self):
        to_remove = self.data[-1]
        self.data.remove(to_remove)
        return to_remove

    def peek(self):
        return ", ".join([el for el in reversed(self.data)])

    def is_empty(self):
        if self.data:
            return False
        return True


# test zero
import unittest


class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push("apple")
        stack.push("carrot")
        self.assertEqual(str(stack), '[carrot, apple]')
        self.assertEqual(stack.pop(), 'carrot')
        self.assertEqual(stack.peek(), 'apple')
        stack.push("cucumber")
        self.assertEqual(str(stack), '[cucumber, apple]')
        self.assertEqual(stack.is_empty(), False)


if __name__ == '__main__':
    unittest.main()