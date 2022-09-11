#!/usr/bin/python3
from calculator_1.py import add, sub, mul, div
import sys
if __name__ == "__main__":
    PEPARGO = len(sys.argv)
    PEMENTO = sys.argv

    if PEPARGO != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        if PEMENTO[2] == "+":
            print("{}".format(PEMENTO))
