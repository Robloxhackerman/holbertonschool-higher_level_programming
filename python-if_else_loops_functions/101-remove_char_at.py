#!/usr/bin/python3
def remove_char_at(str, n):
    PEPEXTO = ""
    for PEPE1 in range(len(str)):
        if PEPE1 == n:
            continue
        else:
            PEPEXTO = PEPEXTO + str[PEPE1]
    return PEPEXTO
