from project.mammal import Mammal
import unittest


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('a', 'b', 'c')

    def test_constructor(self):
        self.assertEqual(self.mammal.name, 'a')
        self.assertEqual(self.mammal.type, 'b')
        self.assertEqual(self.mammal.sound, 'c')
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_get_kingdom(self):
        kingdom = self.mammal.get_kingdom()
        self.assertEqual('animals', kingdom)

    def test_make_sound(self):
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        self.assertEqual(self.mammal.make_sound(), expected)

    def test_info(self):
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        self.assertEqual(self.mammal.info(), expected)

if __name__ == "__main__":
    unittest.main()