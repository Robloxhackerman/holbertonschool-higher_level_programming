#!/usr/bin/python3.4
from hidden_4 import *
if __name__ == "__main__":
    PEPE = dir(hidden_4)
    for PEPE1 in range(len(PEPE)):
        if PEPE[PEPE1][:2] != "__":
            print("{}".format(PEPE1))
