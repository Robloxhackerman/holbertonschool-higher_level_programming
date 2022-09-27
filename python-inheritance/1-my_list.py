#!/usr/bin/python3
"""Bastardito"""

class MyList(list):
    """inherit from list"""
    def print_sorted(self):
        print (list.sort(self))
