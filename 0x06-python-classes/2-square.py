#!/usr/bin/python3
"""class that defines a square attribute"""


class Square:
    """defining a private size instance attribute"""

    def __init__(self, size=0):
        """initializing size instance"""

        self.__size = size
        """making sure size is of type int"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """checking if size is greater than 0"""
        if size < 0:
            raise ValueError("size musy be >= 0")
