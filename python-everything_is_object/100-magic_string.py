#!/usr/bin/python3
def magic_string(PEPE=[0]):
    PEPE[0] += 1
    return str("Holberton, " * (PEPE[0] - 1)) + "Holberton"
