#!/usr/bin/python3
"""Save Object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """Saves a file"""

    with open("filename") as f:
        json.dumps(my_obj, f)
