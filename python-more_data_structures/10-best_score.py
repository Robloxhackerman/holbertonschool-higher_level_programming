#!/usr/bin/python3
def best_score(a_dictionary):
    PEPON = 0
    for PEPE1, PEPE2 in a_dictionary.items():
        if PEPE2 >= PEPON:
            PEPON = PEPE2
    return PEPON
