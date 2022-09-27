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

        if type(attrs) is list and all(type(PEPE1) is str for PEPE1 in attrs):
            for PEPE1 in attrs:
                if PEPE1 in self.__dict__:
                    PEPO.update({PEPE1: self.__dict__[PEPE1]})
            return PEPO
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for PEPE1 in json:
            self.__dict__.update({PEPE1: json[PEPE1]})
