#!/usr/bin/python3
"""Te lo podemos meter?? >///<"""


def add_attribute(obj, attr, value):
    """Metemos atributos"""

    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
