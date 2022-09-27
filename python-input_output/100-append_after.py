#!/usr/bin/python3
"""Insert text"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file"""

    with open(filename, "r") as f:
        PEPE = f.readlines()

    with open(filename, "w") as f2:
        PEPO = ""
        for PEPE1 in PEPE:
            PEPO = PEPO + PEPE1
            if search_string in PEPE1:
                PEPO = PEPO + new_string
        f2.write(PEPO)
