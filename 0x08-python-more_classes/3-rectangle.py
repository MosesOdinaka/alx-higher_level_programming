#!/usr/bin/python3


def __str__(self):
    """Return a string representation of the rectangle"""
    if self.__width == 0 or self.__height == 0:
        return ""
    return "\n".join(["#" * self.__width for _ in range(self.__height)])


def __repr__(self):
    """Return a string representation of the rectangle that can
    be used to recreate the rectangle object"""
    return "Rectangle({}, {})".format(self.__width, self.__height)
