#!/usr/bin/python3
from magic_calulation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
            return c
        else:
            sub(a,b)
