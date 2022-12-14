#!/usr/bin/python3
"""input/output"""


import json


def load_from_json_file(filename):
    """create object from json"""
    with open(filename, 'r') as f:
        return json.load(f)
