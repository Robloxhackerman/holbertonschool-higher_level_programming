#!/usr/bin/python3
"""aaaaaaaaaaaaaaaaaaaa"""


Rectangle = __import__(rectangle).Rectangle

class Square(Rectangle):
    """Aaaaaaaaaaa"""

    def __init__(self, size, x=0, y=0, id=None):
        """aaaaaaaa"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """aaaaaaaaaaaaaaaa"""

        return f"[Square] ({self.id}) {self.__x}/{self.__y} - " \
            f"{self.__size}"

    @property
    def size(self):
        """aaaaaaa"""

        return self.size

    @size.setter
    def size(self, value):
        """aaaaa"""

        self.width = value
        self.height = value
