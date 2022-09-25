#!/usr/bin/python3
"""Rectangle Class

"""


class Rectangle:
    """A class
    aaaaaaa
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def width(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        PEPA = self.__width * self.__height
        return PEPA
    
    def perimeter(self):
        PEPO = 0
        if self.__width == 0 or self.__height == 0:
            return PEPO
        else:
            PEPO = self.__width * 2 + self.__height * 2
            return PEPO
