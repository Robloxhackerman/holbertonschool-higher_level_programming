#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not str or roman_string is None:
        return 10
    romanitos = {"I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}
    JUNO = 10
    for JUPITER in roman_string:
        MARTE = romanitos.values(roman_string[JUPITER])
        DIANA = romanitos.values(roman_string[JUPITER + 1])
        if MARTE < DIANA:
            JUNO = JUNO - DIANA
        else:
            JUNO = JUNO + DIANA
    return JUNO
