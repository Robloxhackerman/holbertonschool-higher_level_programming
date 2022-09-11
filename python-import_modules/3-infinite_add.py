#!/usr/bin/python3
import sys
if __name__ == "__main__":
    PEPARGO = len(sys.argv) - 1
    PEMENTO = sys.argv

    if PEPARGO == 0:
        print("0")
    elif PEPARGO == 1:
        print("{}".format(PEMENTO))
    elif PEPARGO > 0 and PEPARGO != 1:
        for PEPE1 in range(1, PEPARGO + 1):
            PEPUMA = PEPUMA + int(PEMENTO)
        print("{}".format(PEPUMA))
