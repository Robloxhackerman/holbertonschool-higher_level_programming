#!/usr/bin/python3
import sys
if __name__ == "__main__":
    PEPARGO = len(sys.argv) - 1
    PEMENTO = sys.argv

    if PEPARGO == 0:
        print("arguments.")
    elif PEPARGO == 1:
        print("{} argument:".format(PEPARGO))
        for PEPE1 in range(1, PEPARGO):
            print("{}: {}".format(PEPE1, PEMENTO[PEPE1]))
    elif PEPARGO > 0 and PEPARGO != 1:
        print("{} arguments:".format(PEPARGO))
        for PEPE1 in range(1, PEPARGO):
            print("{}: {}".format(PEPE1, PEMENTO[PEPE1]))
