#!/usr/bin/python3
"""input/output"""


import json


def to_json_string(my_obj):
    """json"""
    json_object = json.dumps(my_obj)
    return (json_object)
