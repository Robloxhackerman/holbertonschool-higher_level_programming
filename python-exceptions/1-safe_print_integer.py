#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value is not None:
            print("{:d}".format(value))
        else:
            return False
    except:
        return False
    else:
        return True
