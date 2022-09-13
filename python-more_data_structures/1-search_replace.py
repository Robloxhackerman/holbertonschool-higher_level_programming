#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for PEPE1, PEPE in enumerate(my_list):
        if PEPE == search:
            my_list[PEPE1] = replace
        else:
            continue
    return my_list
