from List.extended_list import IntegerList
import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self) -> None:
        self.example_list = IntegerList(1, 2, 3)

    def test_constructor(self):
        self.example_list = IntegerList('string', 1)
        self.assertEqual(self.example_list.get_data(), [1])

    def test_add_adds_and_returns_list_if_not_int_raise_value_error(self):
        self.example_list.add(5)
        self.assertEqual(self.example_list.get_data(), [1, 2, 3, 5])

    def test_1(self):
        self.assertRaises(ValueError, self.example_list.add, 'string')

    def test_remove_index_return_el_or_index_error(self):
        element = self.example_list.get_data()[0]
        self.assertEqual(self.example_list.remove_index(0), element)

    def test_3(self):
        with self.assertRaises(IndexError):
            self.example_list.remove_index(6)

    def test_get_returns_element_or_index_error(self):
        self.assertEqual(self.example_list.get(0), 1)
        with self.assertRaises(IndexError):
            self.example_list.get(50)

    def test_insert_index_or_value_error(self):
        with self.assertRaises(IndexError):
            self.example_list.insert(5, 10)
        self.example_list.insert(0, 1)
        self.assertEqual(self.example_list.get_data()[0], 1)

    def test_2(self):
        with self.assertRaises(ValueError):
            self.example_list.insert(0, 'string')

    def test_return_biggest_from_get_biggest(self):
        biggest = 3
        self.assertEqual(self.example_list.get_biggest(), biggest)

    def test_return_index_from_el_get_index(self):
        index_of_el = 0
        self.assertEqual(self.example_list.get_index(1), index_of_el)

if __name__ == '__main__':
    unittest.main()