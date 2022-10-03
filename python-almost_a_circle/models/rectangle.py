#!/usr/bin/python3
"""Python Interpreter"""


from models.base import Base


class Rectangle(Base):
    """new class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """new init"""
        self.pitudo(width, "width")
        self.pitudo(height, "height")
        self.pitudo(x, "x")
        self.pitudo(y, "y")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self, width):
        """width of Rectangle"""
        self.__width = width
        return self.__width

    @width.getter
    def width(self):
        """width setter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.pitudo(width, "width")
        self.__width = width
        return self.__width

    @property
    def height(self, height):
        """height of Rectangle"""
        self.__height = height
        return self.__height

    @height.getter
    def height(self):
        """height setter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.pitudo(height, "height")
        self.__height = height
        return self.__height

    @property
    def x(self, x):
        """x of Rectangle"""
        self.__x = x
        return self.__x

    @x.getter
    def x(self):
        """x setter"""
        return self.__x

    @x.setter
    def x(self, x):
        self.pitudo(x, "x")
        """height setter"""
        self.__x = x
        return self.__x

    @property
    def y(self, y):
        """y of Rectangle"""
        self.__y = y
        return self.__y

    @y.getter
    def y(self):
        """y setter"""
        return self.__y

    @y.setter
    def y(self, y):
        """height setter"""
        self.pitudo(y, "y")
        self.__y = y
        return self.__y

    def pitudo(self, value1, value2):
        """hehehe"""

        if type(value1) is not int:
            raise TypeError("{} must be an integer".format(value2))
        if value1 <= 0 and value2 in ("width", "height"):
            raise ValueError("{} must be > 0".format(value2))
        if value1 < 0 and value2 in ("x", "y"):
            raise ValueError("{} must be >= 0".format(value2))

    def area(self):
        """aaaaaaaaaa"""

        areasita = self.__width * self.__height
        return areasita

    def display(self):
        """aaaaaaaa"""

        for PEPE1 in range(self.__height):
            for PEPE2 in range(self.__width):
                print("#", end="")
            print()
