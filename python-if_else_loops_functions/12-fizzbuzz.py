#!/usr/bin/python3
def fizzbuzz():
    for PEPE1 in range(0, 101):
        if (PEPE % 3) == 0 and (PEPE % 5) == 0:
            print(" FizzBuzz")
        elif (PEPE % 5) == 0:
            print(" Buzz")
        elif (PEPE % 3) == 0:
            print(" Fizz")
        else:
            print("{}".format(PEPE1))
