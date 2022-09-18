#!/usr/bin/python3
def safe_print_division(a, b):
    PEPE = 0
    try:
        PEPE = a / b
    except ValueError:
        PEPE = None
    finally:
        print("Inside result: {:.1f}".format(PEPE))
        return PEPE
