#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_list_ints(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([4, 2, 3]), 4)
        self.assertEqual(max_integer([1, 4, 3]), 4)
        self.assertEqual(max_integer([-1, 4, 3]), 4)
        self.assertEqual(max_integer([-1, -4, -3]), -1)
        self.assertEqual(max_integer([3]), 3)

    def test_list_str(self):
        self.assertRaises(TypeError, max_integer, ['a', 6])

    def empty_list(self):
        self.asserRaises(TypeError, max_integer, [])
