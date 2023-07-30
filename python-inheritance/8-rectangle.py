#!/usr/bin/python3
"""
Improve Geometry
"""


class BaseGeometry:
    """empty class"""
    def __init__(self, width, height):
        integer_validator(self.__width, width)
        integer_validator(self.__height, height)
        self.__width = width
        self.__height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
