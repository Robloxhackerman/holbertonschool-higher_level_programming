#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listita = my_list.copy()
    if idx < 0:
        return listita
    elif idx > (len(my_list) - 1):
        return listita
    else:
        listita[idx] = element
        return listita
