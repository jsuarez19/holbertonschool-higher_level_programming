#!/usr/bin/python3
"""
Printing a square
"""


class Square:
    """Create Square class"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[1] < 0 or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[1], int) or not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns area of square"""

        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print(self.__position[1] * '\n', end='')
            for i in range(self.__size):
                print(self.__position[0] * ' ', end='')
                for j in range(self.size):
                    print("#", end='')
                print()
