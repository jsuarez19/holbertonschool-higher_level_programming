#!/usr/bin/python3
"""2. Size validation"""
class Square:
    """A class Square"""
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
