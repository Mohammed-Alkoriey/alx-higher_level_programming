#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """The attriputes of the square class"""
    def __init__(self, size=0):
        """creates a copy of square class"""
        self.__size = size

    def area(self):
        result = self.__size * self.__size
        return result

    @property
    def size(self):
        """Get"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """prints the square's area with hashes"""
        if self.size != 0:
            for i in range(0, self.size):
                for x in range(0, self.size):
                    print("#", end="")
                print("")
        else:
            print("")
