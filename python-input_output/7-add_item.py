#!/usr/bin/python3
"""Load, add, save"""

import json
import os.path
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filesito = "add_item.json"

listita = []

if os.path.exists(filesito) and os.path.getsize(filesito) > 0:
    listita = load_from_json_files(filesito)

if len(sys.argv) > 1:
    for PEPE1 in sys.argv[1:]:
        listita.append(PEPE1)

save_to_json_file(listita, filesito)
