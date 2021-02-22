import unittest
from unittest.mock import patch, mock_open
from pizzeria.dataset import Order

class OrderTestcase(unittest.TestCase):
    def setUp(self):
        self.lines = [
            '5 1 2 1',
            '3 onion pepper basil',
            '3 mushroom tomato basil',
            '3 basil pepper chicken',
            '3 onion chicken tomato',
            '2 basil chicken'
        ]
        self.raw_lines = "\n".join(self.lines)

    def test_create_order(self):
        o = Order.create(self.lines)

        self.assertEqual(o.m, len(self.lines)-1)

    def test_load_from_file(self):
        with patch("builtins.open", mock_open(read_data=self.raw_lines)) as mock_file:
            o = Order.load_from_file("path_to_file")
            self.assertEqual(o.m, len(self.lines)-1)
