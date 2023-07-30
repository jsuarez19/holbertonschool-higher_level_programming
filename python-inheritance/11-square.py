#!/usr/bin/python3
"""
Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class to define a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(size, size)