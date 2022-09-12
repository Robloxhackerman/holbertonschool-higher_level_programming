#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return
    elif idx > len(my_list) - 1:
        return
    else:
        for PEPE1 in range(len(my_list)):
            if idx == PEPE1:
                return my_list[PEPE1]
            else:
                continue
