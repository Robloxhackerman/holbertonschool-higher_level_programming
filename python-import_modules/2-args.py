#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if sys.argv == 0:
        print("arguments.")
    elif sys.argv > 0:
        print("{} arguments:".format(len(argv)))
