#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    PEPARGO = len(argv)
    PEMENTO = argv

    if PEPARGO != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        if PEMENTO[2] == "+":
            print("{}".format(PEMENTO))
