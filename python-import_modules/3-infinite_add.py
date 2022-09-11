#!/usr/bin/python3
import sys
if __name__ == "__main__":
    PEMENTO = sys.argv
    PEPARGO = len(PEMENTO) - 1
    PEPUMA = 0

    if PEPARGO == 0:
        print("0")
    elif PEPARGO == 1:
        print(PEMENTO)
    elif PEPARGO > 0:
        for PEPE1 in range(1, PEPARGO + 1):
            PEPUMA = PEPUMA + int(PEMENTO[PEPARGO])
            print("{}".format(PEPUMA))
