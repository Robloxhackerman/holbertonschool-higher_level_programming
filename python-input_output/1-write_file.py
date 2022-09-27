#!/usr/bin/python3
"""Escribiendo"""


def write_file(filename="", text=""):
    """Writes a file"""

    with open(filename, "w") as f:
        PEPE = f.write(text)
        return PEPE
