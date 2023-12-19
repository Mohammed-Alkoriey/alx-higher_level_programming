#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """The attriputes of the square class"""
    def __init__(self, size=0, position=(0, 0)):
        """creates a copy of square class"""
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """get"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(x) is not int for x in value) or any(z < 0 for z in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
