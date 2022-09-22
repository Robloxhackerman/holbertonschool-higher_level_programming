#!/usr/bin/python3
"""Add

adds two numbers

"""
def add_integer(a, b=98):
    """sumeishon

    adds 2 integers

    Args:
        a (int): value
        b (int): value

    Return:
        a + b

    """

    PEPE = 0

    if type(a) is not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) is not in (int, float):
        raise TypeError("b must be an integer")
    else:
        PEPE = int(a) + int(b)
    return PEPE
