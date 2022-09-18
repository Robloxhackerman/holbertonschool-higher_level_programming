#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) te:
        stderr.write("Exception: {}".format(te))
        return False
    return True
