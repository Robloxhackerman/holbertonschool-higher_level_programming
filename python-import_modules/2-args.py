#!/usr/bin/python3
import sys
if __name__ == "__main__":
    PEPARGO = len(sys.argv)
    if PEPARGO == 0:
        print("arguments.")
    elif PEPARGO > 0:
        print("{} arguments:".format(PEPARGO))
