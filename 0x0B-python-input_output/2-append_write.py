#!/usr/bin/python3
"""
function appends string at end of text file
"""


def append_write(filename="", text=""):
    """appends a text"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
