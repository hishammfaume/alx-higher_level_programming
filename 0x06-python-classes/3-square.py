#!/usr/bin/python3
"""a class that defines a square"""


class Square:
    """instantation"""

    def __init__(self, size=0):
        """makin sure size is an integer"""

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """checking value error"""

        if size < 0:
            raise ValueError("size must be >= 0")
        """area method"""

        """defining area method"""
    def area(self):
        return self.__size ** 2
