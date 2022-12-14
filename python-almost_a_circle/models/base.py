#!/usr/bin/python3
"""pipoaaaaaaaaaaaaaaa"""

import json
import os.path


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

    @classmethod
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

    @staticmethod
    def from_json_string(json_string):
        """aaaaaaaaaaa"""

        if json_string is None or json_string == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            dummy = cls(69)
        if cls.__name__ == "Rectangle":
            dummy = cls(6, 9)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        instances = []
        fileName = cls.__name__ + ".json"
        if os.path.exists(fileName):
            with open(fileName) as tempFile:
                listIntances = []
                obj = cls.from_json_string(tempFile.read())
                for element in obj:
                    listIntances.append(cls.create(**element))
                return listIntances
        else:
            return instances
