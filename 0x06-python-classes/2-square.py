#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """A Square class that has a private instance attribute size"""

    def __init__(self, size=0):
        """Initializes the size attribute of the Square object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
