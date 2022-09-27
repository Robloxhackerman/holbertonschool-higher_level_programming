#!/usr/bin/python3
"""QUe nos deparara el futuro?"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A rectangle"""

    def __init__(self, size):
        """Constructor"""

        self.integer_validator("width", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
