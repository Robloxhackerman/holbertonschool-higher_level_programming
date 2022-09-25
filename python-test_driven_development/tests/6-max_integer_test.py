#!/usr/bin/python3
"""unittests for the function def max_integer(list=[]):
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittests for the function def max_integer(list=[]):"""

    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_one_negative_number_in_the_list(self):
        self.assertEqual(max_integer([1, -2, 3]), 3)

    def test_only_negative_numbers_in_the_list(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_list_of_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_list_is_empty(self):
        self.assertEqual(max_integer([]), None)
