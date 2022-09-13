#!/usr/bin/python3
def search_replace(my_list, search, replace):
    listita = []
    for PEPE1, PEPE in enumerate(my_list):
        if PEPE == search:
            listita.append(replace)
        else:
            listita.append(my_list[PEPE1])
            continue
    return listita
