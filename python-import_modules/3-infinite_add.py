#!/usr/bin/python3
import sys
if __name__ == "__main__":
    PEMENTO = sys.argv
    PEPARGO = len(PEMENTO)
    PEPUMA = 0

    if PEPARGO > 1:
        for PEPE1 in range(1, PEPARGO - 1):
            PEPUMA = PEPUMA + int(PEMENTO[PEPARGO])
    print(PEPUMA)
