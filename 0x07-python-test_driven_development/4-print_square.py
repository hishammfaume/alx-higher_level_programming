#!/usr/bin/python3
"""a function that prints a square with the character #"""

def print_square(size):
    if size > 0:
        print(("#" * size + "\n") * size, end="")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
