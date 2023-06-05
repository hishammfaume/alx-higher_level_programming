#!/usr/bin/python3
"""divides all elements of a matrix"""

def matrix_divided(matrix, div):
    for k in matrix:
        if not isinstance(k,(int, float)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
         if len(k) != len(matrix[0]):
             raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return

