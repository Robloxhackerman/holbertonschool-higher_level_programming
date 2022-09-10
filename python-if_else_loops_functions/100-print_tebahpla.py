#!/usr/bin/python3
for PEPE1 in reversed(range(97, 123)):
    if (PEPE1 % 2 == 0):
        print("{:c}".format(PEPE1), end="")
    else:
        print("{:c}".format(PEPE1 - 32), end="")
