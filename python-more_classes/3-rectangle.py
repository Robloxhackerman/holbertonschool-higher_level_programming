#!/usr/bin/python3
"""
Rectangle aaaaaaaaaaaaaaaaaa
"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """A new instance"""
        self.width = width
        self.height = height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        PEPE = ""
        for PEPE1 in range(self.__height):
            PEPE = PEPE + '\n'
            for PEPE2 in range(self.__width):
                PEPE = PEPE + "#"
        return PEPE

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area"""
        PEPA = self.__width * self.__height
        return PEPA

    def perimeter(self):
        """Calculates the perimeter"""
        PEPO = 0
        if self.__width == 0 or self.__height == 0:
            return PEPO
        else:
            PEPO = self.__width * 2 + self.__height * 2
            return PEPO
