#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    PEPARGO = len(argv) - 1
    PEMENTO = argv

    if PEPARGO != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        if PEMENTO[2] == "+":
            print("{} + {} = {}".format(PEMENTO[1], PEMENTO[3], add(int(PEMENTO[1]), int(PEMENTO[3]))))
        elif PEMENTO[2] == "-":
            print("{} - {} = {}".format(PEMENTO[1], PEMENTO[3], sub(int(PEMENTO[1]), int(PEMENTO[3]))))
        elif PEMENTO[2] == "*":
            print("{} * {} = {}".format(PEMENTO[1], PEMENTO[3], mul(int(PEMENTO[1]), int(PEMENTO[3]))))
        elif PEMENTO[2] == "/":
            print("{} / {} = {}".format(PEMENTO[1], PEMENTO[3], div(int(PEMENTO[1]), int(PEMENTO[3]))))
