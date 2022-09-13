#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b:
        if len(tuple_a) < 2:
            PEPIN = (0,)
            for PEPE1 in range(3):
                tuple_a = tuple_a + PEPIN
        elif len(tuple_b) < 2:
            PEPIN = (0,)
            for PEPE1 in range(3):
                tuple_b = tuple_b + PEPIN
        PEPUM1 = tuple_a[0] + tuple_b[0]
        PEPUM2 = tuple_a[1] + tuple_b[1]
        tuplita = (PEPUM1, PEPUM2)
        return tuplita
    elif tuple_b:
        return tuple_b
    elif tuple_a:
        return tuple_a
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        PEPUM1 = tuple_a[0] + tuple_b[0]
        tuplita = (PEPUM1,)
        return tuplita
    else:
        tuplita = (0, 0,)
        return tuplita
