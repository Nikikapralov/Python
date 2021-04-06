from code import Cat
import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Tom')

    def test_cat_size_increase_after_eat(self):
        start = self.cat.size
        self.cat.eat()
        end = self.cat.size
        self.assertTrue(start < end)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cannot_eat_if_already_fed_raises_error(self):
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_cannot_fall_asleep_if_not_fed_raises_error(self):
        self.cat.fed = False
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
    unittest.main()