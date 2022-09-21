#!/usr/bin/python3
"""Square Class

define a square

"""


class Square:
    """Square

    a square

    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__

        initialize a square

        Attributes:
            size (int): size of square
            position (tuple): position

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

    @property
    def size(self):
        """size

        get the size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """size

        sets the size

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position

        get the position

        """
        return self.__position

    @position.setter
    def position(self, value):
        """position

        set the position

        """
        if self.tuplitas(value):
            self.__position = value
        elif not self.tuplita(value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def tuplita(self, position):
        """tuplita

        check if it is a tuple

        """
        if type(position) is not tuple or len(position) != 2:
            return False
        elif type(position[0]) is not int or position[0] < 0:
            return False
        elif type(position[1]) is not int or position[1] < 0:
            return False
        else:
            return True

    def area(self):
        """area

        calculate the area of a square

        """
        area = self.__size ** 2
        return area

    def my_print(self):
        """my_print

        prints the area

        """
        if self.__size == 0:
            print()
        else:
            for PEPE3 in range(self.__position[1]):
                print()
            for PEPE1 in range(self.__size):
                for PEPE4 inr range(self.__position[0]):
                    print(" ")
                for PEPE2 in range(self.__size):
                    print("#", end="")
                print()
