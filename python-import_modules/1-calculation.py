#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add, sub, mul, div
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
