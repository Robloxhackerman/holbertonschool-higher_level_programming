#!/usr/bin/python3
def safe_print_division(a, b):
    PEPE = 0
    try:
        PEPE = a / b
    except (TypeError, ZeroDivisionError):
        PEPE = None
    finally:
        print("Inside result: {}".format(PEPE))
        return PEPE
