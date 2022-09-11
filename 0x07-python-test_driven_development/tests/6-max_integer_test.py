#!/usr/bin/python3
""" Temp """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_int_basic(self):

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_int_empty(self):

        self.assertEqual(max_integer([]), None)

    def test_max_int_neg(self):

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        
    def test_max_int_one(self):

        self.assertEqual(max_integer([1]), 1)

    if __name__ == '__main__':
        unittest.main()
