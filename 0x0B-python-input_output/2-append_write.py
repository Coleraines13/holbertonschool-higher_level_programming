#!/usr/bin/python3
"""input/output"""


def append_write(filename="", text=""):
    """appen text to files"""
    with open(filename, 'a') as f:
        f.write(text)
        return len(text)
