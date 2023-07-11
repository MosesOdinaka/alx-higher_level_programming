#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): Text to write to the file.
    Returns:
        Written number of characters.
    """
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
