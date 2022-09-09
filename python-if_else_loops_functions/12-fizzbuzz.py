#!/usr/bin/python3
def fizzbuzz():
    print("1 2", end="")
    for PEPE1 in range(3, 101):
        if (PEPE1 % 3) == 0 and (PEPE1 % 5) == 0:
            print(" FizzBuzz",end="")
        elif (PEPE1 % 5) == 0:
            print(" Buzz", end="")
        elif (PEPE1 % 3) == 0:
            print(" Fizz",end="")
        else:
            print(" {}".format(PEPE1),end="")
