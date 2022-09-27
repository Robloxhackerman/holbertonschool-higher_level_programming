#!/usr/bin/python3
"""QUe nos deparara el futuro?"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A rectangle"""

    def __init__(self, size):
        """Constructor"""

        self.integer_validator("width", size)
        super().__init__(size, size)
        self.__size = size
