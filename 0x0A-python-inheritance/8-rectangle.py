#!/usr/bin/pyhton3
"""class inheritance"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""rectangle rep"""

class Rectangle(BaseGeometry):
    """defining the rectanglr"""

    def __init__(self, width, height):
        """instantation"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
