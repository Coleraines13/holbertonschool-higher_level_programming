#!/usr/bin/python3
"""Mylist"""


class Mylist(list):
    """ contains list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
