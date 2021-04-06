from code import Worker
import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Name', 1000, 100)

    def test_check_attributes(self):
        name = 'Name'
        salary = 1000
        energy = 100
        self.assertEqual(self.worker.name, name)
        self.assertEqual(self.worker.salary, salary)
        self.assertEqual(self.worker.energy, energy)

    def test_increment_after_rest(self):
        energy_start = self.worker.energy
        self.worker.rest()
        energy_end = self.worker.energy
        difference = energy_end - energy_start
        expected = 1
        self.assertEqual(difference, expected)

    def test_error_raise_when_negative_or_equal_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_is_salary_increased_correctly(self):
        expected = self.worker.money + self.worker.salary
        self.worker.work()
        self.assertEqual(self.worker.money, expected)

    def test_energy_after_work(self):
        expected = self.worker.energy - 1
        self.worker.work()
        self.assertEqual(self.worker.energy, expected)

    def test_get_info_method_string(self):
        expected = f'{self.worker.name} has saved {self.worker.money} money.'
        self.assertEqual(self.worker.get_info(), expected)


if __name__ == '__main__':
    unittest.main()
