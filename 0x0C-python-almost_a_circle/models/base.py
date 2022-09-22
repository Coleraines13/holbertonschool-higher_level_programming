#!/usr/bin/python3
"""almost a circle"""


class Bass:
    """making class for base shapes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """aatributes for class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
