#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = list(tuple_a)
    tuple_d = list(tuple_b)
    while len(tuple_c) < 2:
        tuple_c.append(0)
    while len(tuple_d) < 2:
        tuple_d.append(0)
    tuplen = (tuple_c[0] + tuple_d[0]), (tuple_c[1] + tuple_d[1])
    return(tuplen)
