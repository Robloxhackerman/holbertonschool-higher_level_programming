#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    diccionarito = a_dictionary.copy()
    for PEPE1, PEPE2 in diccionarito.items():
        diccionarito = PEPE2 * 2
    return diccionarito
