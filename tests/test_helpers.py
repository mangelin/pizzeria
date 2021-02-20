import unittest
from pizzeria.helpers import get_unique_ingredients


class HelpersTestCase(unittest.TestCase):
    # From page 2 of practice_round_2021_v3.pdf
    # Can they be reused?
    SAMPLE_PIZZAS = [
        ['onion', 'pepper', 'olive'],
        ['mushroom', 'tomato', 'basil'],
        ['chicken', 'mushroom', 'pepper'],
        ['tomato', 'mushroom', 'basil'],
        ['chicken', 'basil']
    ]

    SAMPLE_UNIQUE_INGREDIENTS = set([
            "onion",
            "pepper",
            "mushroom",
            "basil",
            "chicken",
            "tomato",
            "olive"
        ])

    def test_unique_ingredients(self):
        pizzas = [
            ["tomato", "mozzarella"],
            ["olives", "tomato"]
        ]
        expected_unique_ingredients = set(["tomato", "mozzarella", "olives"])

        ingredients = get_unique_ingredients(pizzas)

        self.assertEqual(ingredients, expected_unique_ingredients)

    def test_unique_ingredients_sample(self):
        ingredients = get_unique_ingredients(self.SAMPLE_PIZZAS)

        self.assertEqual(
            ingredients,
            self.SAMPLE_UNIQUE_INGREDIENTS)
