import unittest
from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train = Train('a', 1)

    def test_constructor(self):
        self.assertEqual('a', self.train.name)
        self.assertEqual(1, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_train_full(self):
        self.train.passengers = ['bridget']
        with self.assertRaises(ValueError):
            self.train.add('tony')

    def test_add_passenger_passenger_exists_already(self):
        self.train.passengers = ['bridget']
        with self.assertRaises(ValueError):
            self.train.add('bridget')

    def test_add_passenger_correctly(self):
        self.train.add('bridget')
        self.assertEqual(['bridget'], self.train.passengers)

    def test_remove_passenger_error_not_in_list(self):
        with self.assertRaises(ValueError):
            self.train.remove('Bridget')

    def test_remove_passenger_correctly(self):
        self.train.add('bridget')
        self.train.remove('bridget')
        self.assertEqual([], self.train.passengers)



