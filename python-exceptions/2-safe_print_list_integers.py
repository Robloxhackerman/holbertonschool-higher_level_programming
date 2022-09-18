#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    PEPIN = 0
    for PEPE1 in range(x):
        try:
            print("{:d}".format(my_list[PEPE1]), end="")
            PEPIN = PEPIN + 1
        except (ValueError, TypeError):
            PEPE1 = PEPE1 + 1
            continue
    print()
    return PEPIN
