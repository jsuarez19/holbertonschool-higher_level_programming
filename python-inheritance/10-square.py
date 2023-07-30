#!/usr/bin/python3
"""
Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class to define a square"""

    def __init__(self, size):
       super().__init__(size, size)
