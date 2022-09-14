#!/usr/bin/python3
def uniq_add(my_list=[]):
    PEPE = 0
    for PEPE1 in range(len(my_list)):
        aca_ta = my_list.count(my_list[PEPE1])
        if  aca_ta == 1:
            PEPE = PEPE + my_list[PEPE1]
    return PEPE
