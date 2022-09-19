#!/usr/bin/python3
"""Square Class

define a square

"""


class Square:
    """Square

    a square

    """

    def __init__(self, size=0):
        """__init__

        initialize a square

        Attributes:
            size (int): size of square

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """area

        calculate the area of a square

        """
        area = self.__size * self.__size
        return area
