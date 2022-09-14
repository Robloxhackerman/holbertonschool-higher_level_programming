#!/usr/bin/python3
def best_score(a_dictionary):
    PEPON = 0
    PEPONCORE = 0
    if a_dictionary:
        for PEPE1, PEPE2 in a_dictionary.items():
            if PEPE2 >= PEPONCORE:
                PEPONCORE = PEPE2
                PEPON = PEPE1
    return PEPON
