#!/usr/bin/python3
"""inheritance"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""representing the rectangle"""


class Rectangle(BaseGeometry):
    """instantation of the rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    """using the string method"""

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
    """area"""

    def area(self):
        return self.__width * self.__height
