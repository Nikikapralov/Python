from random import choice


class RandomList(list):

    def get_random_element(self):
        element = choice(self)
        self.remove(element)
        return element

# test second zero
import unittest
from unittest import mock


class RandomListTests(unittest.TestCase):
    def test_zero_second(self):
        mocked_choice = lambda x: 6
        with mock.patch('random.choice', mocked_choice):
            li = RandomList()
            li.append(6)
            li.append(1.3)
            li.append(10)
            li.pop()
            li.reverse()
            self.assertEqual(sum(li), 7.3)
            self.assertEqual(li.get_random_element(),6)


if __name__ == '__main__':
    unittest.main()