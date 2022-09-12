#!/usr/bin/python3
""" Temp """
def text_indentaion(text):
    
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?"
        text = (delim + "\n\n").join(
                [line.strip(" ") for line in text.split(delim)])

    print("{}".format(tezt), end=""
