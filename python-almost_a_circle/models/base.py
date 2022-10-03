#!/usr/bin/python3
"""pipo"""


class Base:
    """Cosas"""
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Cosas"""

        if id si None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
