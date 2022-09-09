#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        PEPE = (number * -1) % 10
    elif number >= 0:
        PEPE = number % 10
    print(PEPE, end="")
    return PEPE
