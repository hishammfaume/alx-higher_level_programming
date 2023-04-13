#!/usr/bin/python3
"""inherits from 9-rectangle"""

Rectangle = __import__("9-rectangle").Rectangle
"""square class"""

class Square(Rectangle):
    """representing the size of the square"""
    def __init__(self, size):
        """instantation"""
        self.__size = size
        self.integer_validator("size", size)
    """showing the rectangle"""

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
    """the area"""
    
    def area(self):
        return self.__size * self.__size
