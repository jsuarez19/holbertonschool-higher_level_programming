#!/usr/bin/python3
"""
Divide a matrix
"""


def matrix_divided(matrix, div):
    """Divides all element by div"""
    for row in matrix:
        for x in row:
            if not isinstance(x, (float, int)):
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")

    sameSize = len(matrix[0])
    for row in matrix:
        if len(row) != sameSize:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elemento / div, 2) for elemento in row] for row in matrix]

    return new_matrix
