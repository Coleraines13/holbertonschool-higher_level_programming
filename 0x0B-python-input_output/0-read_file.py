#!usr/bin/python3
"""this reads a filename and wirtes its contents into and output"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        for i in f:
            print("{}".format(i), end="")
