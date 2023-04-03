#!/usr/bin/python3
"""a class that defines a rectangle"""


class Rectangle():
    """public class attribute"""

    print_symbol = "#"
    number_of_instances = 0

    """private instance"""

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    """prints when an instance is deleted"""
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """public instantation area method"""
    def area(self):
        return self.__height*self.__width

    """public instantation perimeter methid"""
    def perimeter(self):
        if self.__width == 0 | self.__height == 0:
            return 0
        return (self.__height+self.__width)*2

    def __str__(self):
        """prints a rectangle representation with #"""
        rep = ""
        if self.__height != 0 and self.__width != 0:
            rep += "\n".join(str(self.print_symbol) * self.__width for i in range(self.__height))
        return rep

    def __repr__(self):
        """prints a representation to be able to create a new instance"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
