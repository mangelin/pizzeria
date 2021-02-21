import unittest
from pizzeria.helpers import get_unique_ingredients, calculate_score

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

    def test_calculate_score(self):
        pizzas_to_deliver = [
            [1, 4],         # score: 16
            [0, 2, 3]       # score: 49
        ]

        result = calculate_score([pizzas_to_deliver[0]], PIZZAS)
        self.assertEqual(result, 16)

        result = calculate_score([pizzas_to_deliver[1]], PIZZAS)
        self.assertEqual(result, 49)

        result = calculate_score(pizzas_to_deliver, PIZZAS)
        self.assertEqual(result, 65)

