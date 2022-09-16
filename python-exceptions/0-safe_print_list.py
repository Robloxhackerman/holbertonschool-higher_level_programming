#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    PEPIN = 0
    try:
        for PEPE1 in my_list:
            if PEPIN < x:
                print("{}".format(my_list[PEPIN]), end="")
            PEPIN = PEPIN + 1
        print()
    except TypeError:
        pass
    finally:
        return PEPIN
