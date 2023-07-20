#!/usr/bin/python3
"""2. Size validation"""
class Square:
    """A class Square"""
    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            if isinstance(size, int):
                self.__size = size
            else:
                raise TypeError
        except TypeError:
            print("size must be an integer")
