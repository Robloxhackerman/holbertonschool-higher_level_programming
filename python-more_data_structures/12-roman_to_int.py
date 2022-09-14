#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not str or roman_string is None:
        return 0
    romanitos = [["I", 1], ["V", 5], ["X", 10], ["L", 50],
            ["C", 100], ["D", 500], ["M", 1000]]

    for PEPE1 in roman_string:
        for PEPE2 in romanitos:
            if PEPE1 == PEPE1[0]:
