#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    PEPARGO = len(argv) - 1
    PEMENTO = argv

    if PEPARGO != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if PEMENTO[2] == "+":
            PEPE = add(int(PEMENTO[1]), int(PEMENTO[3]))
            print("{} + {} = {}".format(PEMENTO[1], PEMENTO[3], PEPE))
        elif PEMENTO[2] == "-":
            PEPE = sub(int(PEMENTO[1]), int(PEMENTO[3]))
            print("{} - {} = {}".format(PEMENTO[1], PEMENTO[3], PEPE))
        elif PEMENTO[2] == "*":
            PEPE = mul(int(PEMENTO[1]), int(PEMENTO[3]))
            print("{} * {} = {}".format(PEMENTO[1], PEMENTO[3], PEPE))
        elif PEMENTO[2] == "/":
            PEPE = div(int(PEMENTO[1]), int(PEMENTO[3]))
            print("{} / {} = {}".format(PEMENTO[1], PEMENTO[3], PEPE))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
