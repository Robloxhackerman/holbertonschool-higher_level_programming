#!/usr/bin/python3
"""Rompiendo malos"""


def say_my_name(first_name, last_name=""):
    """ Prints a name"""

    if first_name is not str or last_name is not str:
        raise TypeError("first_name must be a string or last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
