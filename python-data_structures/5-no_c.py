#!/usr/bin/python3
def no_c(my_string):
    listita = ""
    for PEPE1 in range(len(my_string)):
        if my_string[PEPE1] == "c" or my_string[PEPE1] == "C":
            continue
        else:
            listita = listita + my_string[PEPE1]
    return listita
