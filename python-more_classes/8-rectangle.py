#!/usr/bin/python3
"""
Rectangle aaaaaaaaaaaaaaaaaa
"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """A new instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        PEPE = ""
        for PEPE1 in range(self.__height):
            if PEPE1 > 0:
                PEPE = PEPE + '\n'
            for PEPE2 in range(self.__width):
                PEPE = PEPE + str(self.print_symbol)
        return PEPE

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Bigger or equals? ;|"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area() or rect_1.area() is rect_2.area():
            return rect_1
        else:
            return rect_2
