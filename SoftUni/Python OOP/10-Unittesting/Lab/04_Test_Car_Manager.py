from CarManager.car_manager import Car
import unittest


class TestCarManager(unittest.TestCase):
    def setUp(self):
        self.car = Car('Make', 'Model', 1, 100)

    def test_constructor(self):
        self.assertEqual(self.car.make, 'Make')
        self.assertEqual(self.car.model, 'Model')
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 100)

    def test_make_cannot_be_null_or_empty(self):
        with self.assertRaises(Exception):
            car = Car('', 'Model', 1, 100)

    def test_model_cannot_be_null_or_empty(self):
        with self.assertRaises(Exception):
            car = Car('Make', '', 1, 100)

    def test_fuel_consumption_not_0_or_negative(self):
        with self.assertRaises(Exception):
            car = Car('Make', 'Model', 0, 100)

        with self.assertRaises(Exception):
            car = Car('Make', 'Model', -1, 100)

    def test_fuel_capacity_cannot_0_or_negative(self):
        with self.assertRaises(Exception):
            car = Car('Make', 'Model', 1, 0)

        with self.assertRaises(Exception):
            car = Car('Make', 'Model', 1, -1)

    def test_fuel_amount_cannot_be_negative(self):
        with self.assertRaises(Exception):
            self.car.fuel_amount = -1

    def test_refuel_adds_correct_fuel_to_fuel_amount_above_capacity(self):
        self.car.refuel(1000)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_refuel_adds_correct_fuel_to_fuel_amount_does_not_exceed_capacity(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_refuel_amount_cannot_be_negative_or_0(self):
        with self.assertRaises(Exception):
            self.car.refuel(-1)

        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_drive_fuel_left_is_correct(self):
        self.car.fuel_amount = 1
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_drive_cannot_make_the_drive(self):
        with self.assertRaises(Exception):
            self.car.drive(1)





if __name__ == '__main__':
    unittest.main()