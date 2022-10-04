#!/usr/bin/python3
"""pipoaaaaaaaaaaaaaaa"""

import json


class Base:
    """Cosas"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Cosas"""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """aaaaaaaaaaaaa"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """aaaaa"""

        filesito = cls.__name__ + ".json"

        with open(filesito, "w") as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            listita = []

            for PEPE1 in list_objs:
                listita.append(PEPE1.to_dictionary())

            return f.write(cls.to_json_string(listita))
