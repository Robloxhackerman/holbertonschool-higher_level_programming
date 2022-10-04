#!/usr/bin/python3
"""aaaaaaaaaaaaaaaaaaaa"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """Aaaaaaaaaaa"""

    def __init__(self, size, x=0, y=0, id=None):
        """aaaaaaaa"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """aaaaaaaaaaaaaaaa"""

        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """aaaaaaa"""

        return self.width

    @size.setter
    def size(self, value):
        """aaaaa"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Papo pe parabi pa pa pa po"""
        larguito = len(args)
        listita = ["id", "size", "x", "y"]

        if larguito > 0:
            for PEPE1 in range(larguito):
                setattr(self, listita[PEPE1], args[PEPE1])
        if len(kwargs) > 0:
            for PEPE1, PEPE2 in kwargs.items():
                if PEPE1 in listita:
                    setattr(self, PEPE1, PEPE2)
