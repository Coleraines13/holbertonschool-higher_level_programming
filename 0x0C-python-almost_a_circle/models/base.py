#!/usr/bin/python3
"""almost a circle"""
import json
from os.path import exists


class Base:
    """making class for base shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """aatributes for class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert to json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save class info to json file"""
        json_list = []
        filename = cls.__name__ + '.json'
        if list_objs is not None:
            for i in list_objs:
                json_list.append(cls.to_dictionary(i))
            with open(filename, 'w') as f:
                f.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """list of json string"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """added and updated dummy values to subclass"""
        if cls.__name__ == "Square":
            dummy = cls(4)
        if cls.__name__ == "Rectangle":
            dummy = cls(4, 4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of all instances of subclass"""
        filename = cls.__name__ = ".json"
        json_list = []
        with open(filename, 'r') as f:
            jason_list = cls.from_json_string(f.read())
            for i, j in enumerate(json_list):
                json_list[i] = cls.create(**jason_list[i])
            return jason_list
