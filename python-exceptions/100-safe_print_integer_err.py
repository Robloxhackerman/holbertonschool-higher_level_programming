#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) PEPOTE:
        stderr.write("Exception: {}".format(PEPOTE))
        return False
    return True
