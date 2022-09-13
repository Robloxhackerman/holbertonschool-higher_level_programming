#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listita = []
    for PEPE1 in range(len(my_list)):
        if my_list[PEPE1] % 2 == 0:
            listita[PEPE1] = True
        else:
            listita[PEPE1] = False
