#!/usr/bin/python3
"""Twins or another thing"""


def is_kind_if_class(obj, a_class):
    """Same class or inherit from"""
    if issubclass(obj, a_clas) or type(obj) == a_class:
        return True
    else:
        return False
