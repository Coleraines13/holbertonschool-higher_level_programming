#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        new = my_string.translate({ord('C'): ""})
        new2 = new.translate({ord('c'): ""})
        return (new2)
