#!/usr/bin/python3
"""ABBA > 2000s music"""


def print_square(size):
    """Prints a square with #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) == float:
        raise TypeError("size must be an integer")

    for PEPE1 in range(size):
        for PEPE2 in range(size):
            print("#", end="")
        print()
