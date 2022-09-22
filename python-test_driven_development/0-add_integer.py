#!/usr/bin/python3
def add_integer(a, b=98):
    PEPE = 0

    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        PEPE = a + b
