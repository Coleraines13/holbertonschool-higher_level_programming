#!/usr/bin/python3
"""input/output"""


import json


def save_to_json_file(my_obj, filename):
    """write from json to python"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
