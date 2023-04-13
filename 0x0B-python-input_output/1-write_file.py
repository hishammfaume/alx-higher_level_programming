#!/usr/bin/python3
"""
writes a string to a text file returns the number of characters written
"""


def write_file(filename="", text=""):
    """returns number of characters of written text"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
