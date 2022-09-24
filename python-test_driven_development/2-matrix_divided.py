#!/usr/bin/python3
"""Divides a matrix"""


def matrix_divided(matrix, div):
    """Divides a matrix"""

    matrizita = []

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    PEPARGO = len(matrix[0])
    
    for PEPE1 in matrix:
        matrizita2 = []
        
        if PEPARGO != len(PEPE1):
            raise TypeError("Each row of the matrix must have the same size")
        PEPARGO = len(PEPE1)
        
        for PEPE2 in PEPE1:
            if type(PEPE2) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            PEPE = PEPE2 / div
            matrizita2.append(round(PEPE, 2))
        matrizita.append(matrizita2)

        return matrizita
