#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """The attriputes of the square class"""
    def __init__(self, size=0):
        """creates a copy of square class"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
    def area(self):
        result = self.__size * self.__size
        return result
