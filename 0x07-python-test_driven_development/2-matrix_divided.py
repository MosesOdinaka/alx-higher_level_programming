#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to divide.
        div (int, float): The number to divide the matrix by.

    Returns:
        list of lists: A new matrix with the result of the division.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
            if the rows of the matrix are not all the same size,
            or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for
                                               row in matrix):
        raise TypeError("matrix must be a matrix(list of lists) of
                        integers/floats")
    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix(list of lists) of
                        integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
