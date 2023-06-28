#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """A Square class that has a private instance attribute size"""

    def __init__(self, size=0):
        """Initializes the size attribute of the Square object"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
