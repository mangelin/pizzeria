import unittest
from pizzeria.helpers import get_unique_ingredients

PIZZAS = [
    ['onion','pepper','olive'],
    ['mushroom','tomato','basil'],
    ['chicken','mushroom','pepper'],
    ['tomato','mushroom','basil'],
    ['chicken','basil']
]

class HelpersTestCase(unittest.TestCase):
    def test_unique_ingredients(self):
        orders = [0]

        ingredients = get_unique_ingredients(orders, PIZZAS)

        self.assertEqual(ingredients,set(PIZZAS[0]))

    
    def test_unique_all_ingredients(self):
        orders = [0,1,2,3,4]

        result = get_unique_ingredients(orders, PIZZAS)

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
    
