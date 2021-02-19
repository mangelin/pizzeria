import unittest
from pizzeria.helpers import get_unique_ingradients
from pizzeria.types import PIZZAS


class HelpersTestCase(unittest.TestCase):
    def test_unique_ingradients(self):
        pizzas = [0]

        ingradients = get_unique_ingradients(pizzas)

        self.assertEqual(ingradients,set(PIZZAS[0]))

    
    def test_unique_all_ingradients(self):
        pizzas = [0,1,2,3,4]

        result = get_unique_ingradients(pizzas)

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
    
