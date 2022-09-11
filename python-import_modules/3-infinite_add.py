#!/usr/bin/python3
import sys
if __name__ == "__main__":
    PEPARGO = len(sys.argv) - 1
    PEMENTO = sys.argv
    PEPUMA = 0

    elif PEPARGO > 1:
        for PEPE1 in range(1, PEPARGO):
            PEPUMA = PEPUMA + int(PEMENTO[PEPARGO])
    print("{}".format(PEPUMA))
