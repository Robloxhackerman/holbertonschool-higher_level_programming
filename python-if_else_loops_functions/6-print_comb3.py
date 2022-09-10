#!/usr/bin/python3

for PEPE1 in range(0, 10):
    for PEPE2 in range(0, 10):
        if (PEPE1 != PEPE2 and PEPE1 < PEPE2) and PEPE1 < 9:
            if PEPE1 == 8 and PEPE2 == 9:
                print("{}{}".format(PEPE1, PEPE2))
            else:
                print("{}{}, ".format(PEPE1, PEPE2), end="")
