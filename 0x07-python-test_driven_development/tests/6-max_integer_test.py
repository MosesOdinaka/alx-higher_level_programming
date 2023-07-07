#!/usr/bin/python3

import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)

    def test_max_integer_empty(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_non_list(self):
        with self.assertRaises(TypeError):
            max_integer("not a list")
        with self.assertRaises(TypeError):
            max_integer(12)


if __name__ == '__main__':
    unittest.main()
