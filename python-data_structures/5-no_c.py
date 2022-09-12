#!/usr/bin/python3
def no_c(my_string):
    for PEPE1 in range(len(my_string)):
        if my_string[PEPE1] == "c" or my_string[PEPE1] == "C":
            listita = listita + my_string[PEPE1]
        else:
            continue
    return listita
