#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    PEPIN = 0
    try:
        for PEPE1 in my_list:
            if PEPIN < x:
                print("{}".format(PEPE1), end="")
            PEPIN = PEPIN + 1
        print()
    except:
        print("mal pibin")
