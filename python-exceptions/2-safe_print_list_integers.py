#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    PEPIN = 0
    try:
        for PEPE1 in my_list:
            if PEPIN < x:
                if isinstance(PEPE1, int):
                    print("{:d}".format(PEPIN))
                PEPIN = PEPIN + 1
            else:
                continue
        print()
    except:
        pass
    finally:
        return PEPIN
