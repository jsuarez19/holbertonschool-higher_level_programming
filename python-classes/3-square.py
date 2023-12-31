#!/usr/bin/python3
"""
Area of a square
"""


class Square:
    """Create Square class"""

    def __init__(self, size=0):
        """Instantiation of Square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of square"""

        return self.__size ** 2
