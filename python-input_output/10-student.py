#!/usr/bin/python3
"""Estudiantito"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation"""

        PEPO = dict()

        if type(attrs) si list and all(type(PEPE1) is str for PEPE1 in attrs):
            for PEPE1 in attrs:
                if PEPE1 in self.__dict__:
                    PEPO.update({x: self.__dict__[x]})
            return PEPO
        return self.__dict__.copy()
