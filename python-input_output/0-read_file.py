#!/usr/bin/python3
"""Metiendo y sacando"""


def read_file(filename=""):
    """Reads a file and prints it to stdout"""

    with open(filename, encoding="utf-8") as f:
        PEPE = f.read()
        print(PEPE, end="")
