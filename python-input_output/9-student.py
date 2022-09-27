#!/usr/bin/python3
"""Estudiantito"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation"""

        return self.__dict__
