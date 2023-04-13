#!/usr/bin/python3
"""
inherits from 9-rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


"""square class"""


class Square(Rectangle):
    """representation of the square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    """area of the square"""

    def area(self):
        return self.__size * self.__size
    """representation using str"""

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
