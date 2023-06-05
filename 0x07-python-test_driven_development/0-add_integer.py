#!/usr/bin/python3
"""Adds two integers together."""


def add_integer(a, b=98):
    """checking if a and b are integers or floats"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    """addition of two integer values"""
    return a + b
