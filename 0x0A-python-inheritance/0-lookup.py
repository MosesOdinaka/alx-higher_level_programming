#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: The object to inspect

    Returns:
        A list object containing the names of the available attributes
    """
    return dir(obj)
