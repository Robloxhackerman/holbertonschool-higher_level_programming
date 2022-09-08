#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
PEPE = number % 10
if PEPE == 0:
    print(f"Last digit of {number} is {PEPE} and is 0")
elif PEPE > 5:
    print(f"Last digit of {number} is {PEPE} and is greater than 5")
elif PEPE < 6 and PEPE != 0:
    print(f"Last digit of {number} is {PEPE} and is less than 6 and not 0")
