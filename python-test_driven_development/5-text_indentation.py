#!/usr/bin/python3
"""Python-matron

prints text

"""


def text_indentation(text):
    """ prints a text with 2
        new lines after each '.?:'
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    PEPE = False
    PEPIN = 0
    for PEPE1 in range(len(text)):
        if text[PEPE1] is in ".?:":
            PEPE = False
            PEPON = PEPE1 + 1
            print(text[PEPIN:PEPON].lstrip(), end='\n\n')
            PEPIN = PEPON
        if PEPE is True and PEPE1 == len(text) - 1:
            print(text[PEPIN:].lstrip(), end="")

    if PEPE is False:
        print(text.lstrip(), end="")
