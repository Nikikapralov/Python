import unittest
from project.rooms.room import Room


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room('a', 1000.0, 2)

    def test_constructor(self):
        self.assertEqual(self.room.family_name, 'a')
        self.assertEqual(self.room.budget, 1000.0)
        self.assertEqual(self.room.members_count, 2)
        self.assertEqual(self.room.children, [])
        self.room.expenses = 500.0
        self.assertEqual(self.room.expenses, 500.0)

    def test_expenses_raises_error_if_negative(self):
        with self.assertRaises(ValueError):
            self.room.expenses = -100

    def test_calculate_expenses_calculates_correctly(self):
        c = Child(10.0, 10.0, 10.0)
        f = Fridge()
        children_list = [c]
        appliances_list = [f]
        self.assertEqual(self.room.calculate_expenses(children_list, appliances_list), 31.2)

if __name__ == '__main__':
    unittest.main()
