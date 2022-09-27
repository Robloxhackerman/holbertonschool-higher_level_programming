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

        PEPE = self.__dict__
        PEPO = dict()

        if type(attrs) is list:
            for PEPE1 in attrs:
                if type(PEPE1) is not str:
                    return PEPE
                if PEPE1 in PEPO:
                    PEPO[PEPE1] = PEPE[PEPE1]
            return PEPO
        return PEPE
