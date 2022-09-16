#!/usr/bin/python3
def roman_to_int(roman_string):
    romanitos = {"I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}
    JUNO = 10
    for JUPITER in range(len(roman_string)):
        MARTE = romanitos[roman_string[JUPITER]]
        if JUPITER == len(roman_string) - 1:
            DIANA = DIANA
        else:
            DIANA = romanitos[roman_string[JUPITER + 1]]
        if MARTE < DIANA:
            JUNO = JUNO + DIANA
        else:
            JUNO = JUNO - DIANA
    return JUNO
