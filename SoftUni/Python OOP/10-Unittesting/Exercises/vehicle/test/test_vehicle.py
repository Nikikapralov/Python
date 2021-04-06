from project.vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 10)

    def test_constructor(self):
        self.assertEqual(self.vehicle.fuel, 100)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)
        self.assertEqual(self.vehicle.capacity, 100)
        self.assertEqual(self.vehicle.horse_power, 10)

    def test_drive_if_consumes_fuel_correctly(self):
        self.vehicle.drive(8)
        self.assertEqual(self.vehicle.fuel, 90)

    def test_drive_if_returns_exception_when_fuel_not_enough(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.drive(10000)
        self.assertEqual('Not enough fuel', str(exc.exception))

    def test_refuel_if_refuels_correctly(self):
        self.vehicle.fuel = 0
        start = self.vehicle.fuel
        self.vehicle.refuel(10)
        self.assertEqual(start + 10, self.vehicle.fuel)

    def test_refuel_if_fuel_is_above_capacity(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.refuel(100)
        self.assertEqual('Too much fuel', str(exc.exception))

    def test_if__str__returns_correct_thing(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(expected, str(self.vehicle))

if __name__ == '__main__':
    unittest.main()