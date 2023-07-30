#!/usr/bin/python3
"""
Square
"""


Rectangle = __import__("9-base_geometry").Rectangle


class Square(Rectangle):
    """Class to define a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
