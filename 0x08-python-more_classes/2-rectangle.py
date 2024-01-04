#!/usr/bin/python3
"""A representation of a square"""


class Rectangle():
    """Square class properties"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width_setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height_setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        are = self.width * self.height
        return are

    def perimeter(self):
        if self.width == 0 || self.height == 0:
            per = 0
        else:
            per = (2 * self.width) + (2 * self.height)

        return per
