#!/usr/bin/python3
def uniq_add(my_list=[]):
    PEPE = 0
    for PEPE1 in range(len(my_list)):
        for PEPE2 in range(len(my_list)):
            if my_list[PEPE1] == my_list[PEPE2]:
                continue
            else:
                PEPE = my_list[PEPE1]
    return PEPE
