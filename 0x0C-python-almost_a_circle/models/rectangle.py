#!/usr/bin/python3
"""module for Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.attr_valid("width", value, False)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.attr_valid("height", value, False)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.attr_valid("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.attr_valid("y", value)
        self.__y = value

    def attr_valid(self, attr, val, equal=True):
        '''Method for validating the attribute.'''
        if type(val) is not int:
            raise TypeError("{} must be an integer".format(attr))
        if equal and val < 0:
            raise ValueError("{} must be >= 0".format(attr))
        elif not equal and val <= 0:
            raise ValueError("{} must be > 0".format(attr))

    def area(self):
        return self.width * self.height
