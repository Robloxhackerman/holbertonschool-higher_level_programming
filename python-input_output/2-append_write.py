#!/usr/bin/python3
"""Agregando"""


def append_write(filename="", text=""):
    """appends string at the end of a file"""

    with open(filename, "a") as f:
        PEPE = f.write(text)
        return PEPE
