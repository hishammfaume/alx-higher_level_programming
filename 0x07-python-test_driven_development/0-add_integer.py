#!/usr/bin/python3
"""Adds two integers together."""


def add_integer(a, b=98):
    """checking if a and b are integers or floats"""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    """addition of two integer values"""
    return a+b
