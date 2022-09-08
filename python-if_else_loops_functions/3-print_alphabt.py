#!/usr/bin/python3

PEPE = "{:c}"
for PEPE1 in range(97, 123):
    if PEPE1 == 101:
        continue
    elif PEPE1 == 113:
        continue
    else:
        print(PEPE.format(PEPE1), end='')
