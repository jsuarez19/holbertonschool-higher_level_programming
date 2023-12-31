#!/usr/bin/python3
"""
This py will define a square class.
"""


class Square:
    """A class Square"""

    def __init__(self, size=0):
        """Initialize an Square

        Args:
            size (int): The square's size
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
