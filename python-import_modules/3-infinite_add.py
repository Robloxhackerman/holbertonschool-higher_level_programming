#!/usr/bin/python3
import sys
if __name__ == "__main__":
    PEPUMA = 0
    for PEPE1 in range(1, len(sys.argv)):
        PEPUMA = PEPUMA + int(sys.argv[PEPE1])
    print("{}".format(PEPUMA))
