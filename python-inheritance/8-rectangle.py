#!/usr/bin/python3
"""QUe nos deparara el futuro?"""


class BaseGeometry():
    """An empty class"""

    def area(self):
        """Raise an error"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """A rectangle"""

    def __init__(self, width, height):
        """Constructor"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
