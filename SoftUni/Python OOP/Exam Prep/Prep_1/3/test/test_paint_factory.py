import unittest
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.factory = PaintFactory('a', 10)

    def test_constructor(self):
        self.assertEqual(self.factory.name, 'a')
        self.assertEqual(self.factory.capacity, 10)
        self.assertEqual(self.factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
        self.assertEqual(self.factory.ingredients, {})

    def test_add_invalid_ingredient(self):
        with self.assertRaises(TypeError) as exc:
            self.factory.add_ingredient('brrr', 1)

    def test_add_quantity_above_capacity(self):
        with self.assertRaises(ValueError) as exc:
            self.factory.add_ingredient('white', 100)


    def test_ingredient_not_ingredientsdict_add_it_to_dict_then_add_quantity(self):
        self.factory.add_ingredient('white', 1)
        self.assertEqual(self.factory.ingredients['white'], 1)

    def test_remove_ingredient_cannot_be_less_than_zero(self):
        self.factory.add_ingredient('white', 1)
        with self.assertRaises(ValueError) as exc:
            self.factory.remove_ingredient('white', 6)


    def test_remove_ingredient_works_as_expected(self):
        self.factory.add_ingredient('white', 1)
        self.factory.remove_ingredient('white', 1)
        self.assertEqual(0, self.factory.ingredients['white'])

    def test_products_return_ingredients_dict(self):
        self.assertEqual(self.factory.products, self.factory.ingredients)

    def test_can_add(self):
        self.assertEqual(self.factory.can_add(1), True)
        self.factory.add_ingredient('white', 10)
        self.assertEqual(self.factory.can_add(1), False)


