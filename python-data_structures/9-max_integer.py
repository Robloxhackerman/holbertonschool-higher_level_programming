#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        PEPOTE = 0
        for PEPE1 in range(len(my_list) - 1):
            if my_list[PEPE1] >= PEPOTE:
                PEPOTE = my_list[PEPE1]
                return PEPOTE
            else:
                continue
