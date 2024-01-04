#!/usr/bin/python3
"""A representation of a square"""


class Rectangle():
    """Square class properties"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            return ""

        for x in range(0, self.height):
            for y in range(0, self.width):
                hashed.append(str(self.print_symbol))
            hashed.append("\n")

        hashed.pop()
        return "".join(hashed)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
