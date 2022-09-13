#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        PEPIN = (0,)
        for PEPE1 in range(len(tuple_a)):
            tuple_a = tuple_a + PEPIN
    elif len(tuple_b) < 2:
        PEPIN = (0,)
        for PEPE1 in range(len(tuple_b)):
            tuple_b = tuple_b + PEPIN

    PEPUM1 = tuple_a[0] + tuple_b[0]
    PEPUM2 = tuple_b[0] + tuple_b[1]
    tuplita = (PEPUM1, PEPUM2,)
    return tuplita
