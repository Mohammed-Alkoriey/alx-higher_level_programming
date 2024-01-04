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

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
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
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * self.width) + (2 * self.height)

    def __str__(self):
        hashed = []

        if self.width == 0 or self.height == 0:
            return ''

        for (x in range(0, self.height)):
            for (y in range(0, self.width)):
                hashed.append("#")
            hashed.append("\n")

        hashed.pop()
        return "".join(hashed)
