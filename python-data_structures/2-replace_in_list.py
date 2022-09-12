#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        for PEPE1 in range(len(my_list)):
            if idx == PEPE1:
                return my_list[PEPE1] = element
            else:
                continue
