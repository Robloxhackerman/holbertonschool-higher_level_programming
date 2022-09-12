#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for PEPE1 in matrix:
            PEPE2 = 1
            PEPARGO = len(PEPE1)
            for PEPE3 in PEPE1:
                if PEPE2 == PEPARGO:
                    print("{:d}".format(PEPE3), end="")
                else:
                    print("{:d}".format(PEPE3), end=" ")
                PEPE2 = PEPE2 + 1
            print()
