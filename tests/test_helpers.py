import unittest
from pizzeria.helpers import get_unique_ingredients
from pizzeria.types import PIZZAS


class HelpersTestCase(unittest.TestCase):
    def test_unique_ingredients(self):
        pizzas = [0]

        ingredients = get_unique_ingredients(pizzas)

        self.assertEqual(ingredients,set(PIZZAS[0]))

    
    def test_unique_all_ingredients(self):
        pizzas = [0,1,2,3,4]

        result = get_unique_ingredients(pizzas)

        expected_result = set(sorted([
            "onion",
            "pepper",
            "mushroom",
            "basil",
            "chicken",
            "tomato",
            "olive"
        ]))

        self.assertEqual(result, expected_result)
    
