#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    PEPIN = 0
    NASTY = 0
    try:
        for PEPE1 in my_list:
            if PEPIN < x:
                if isinstance(PEPE1, int):
                    NASTY = NASTY + 1
                    print("{:d}".format(my_list[PEPIN]), end="")
                PEPIN = PEPIN + 1
            else:
                continue
        print()
    except:
        pass
    finally:
        return NASTY
