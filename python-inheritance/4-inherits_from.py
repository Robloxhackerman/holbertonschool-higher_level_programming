#!/usr/bin/python3
"""Sisoy"""


def inherits_from(obj, a_class):
    """Checks if obj is instance of class that
    inherited from a specified class"""

    return (isinstance(obj, a_class) and type(obj) != a_class)
