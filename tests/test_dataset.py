import unittest
from pizzeria.dataset import Order

class OrderTestcase(unittest.TestCase):
    def setUp(self):
        self.lines = [
            '5 1 2 1',
            '3 onion pepper basil',
            '3 mushromm tomato basil',
            '3 basil pepper chicken',
            '3 onion chicken tomato',
            '2 basil chicken'
        ]

    def test_create_order(self):
        o = Order.create(self.lines)

        self.assertEqual(o.m, len(self.lines)-1)