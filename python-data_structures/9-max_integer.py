#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        PEPOTE = -10000
        for PEPE1 in range(len(my_list)):
            if my_list[PEPE1] >= PEPOTE:
                PEPOTE = my_list[PEPE1]
            else:
                continue
        return PEPOTE
