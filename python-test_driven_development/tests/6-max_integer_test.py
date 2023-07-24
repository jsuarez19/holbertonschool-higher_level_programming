#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_list_ints(self):
        result = max_integer([1, 2, 3])
        self.assertEqual(result, 3)

    def test_list_str(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 'n'])

