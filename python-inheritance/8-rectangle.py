#!/usr/bin/python3
"""
Rectangle
"""


class Rectangle(BaseGeometry):
    """Class to define a rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
