#!/usr/bin/python3
"""Square Class

defines a square

"""


class Square:
    """Square

    a square

    """

    def __init__(self, size=0):
        """__init__

        initialize a square

        Attributes:
            size (int): size of the square

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size bust be >= 0")
        self.__size = size
