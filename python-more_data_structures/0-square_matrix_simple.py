#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrisita = []
    for PEPE in matrix[:]:
        matrisita.append(list(map(lambda x : x ** 2, PEPE)))
    return matrisita
