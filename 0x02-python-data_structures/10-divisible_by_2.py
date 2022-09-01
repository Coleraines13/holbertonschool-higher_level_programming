#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list is None:
        return(my_list)
    else:
        values = []
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                values.append(True)
            else:
                values.append(False)
        return(values)
