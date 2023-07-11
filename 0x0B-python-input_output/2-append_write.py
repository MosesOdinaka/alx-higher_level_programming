#!/usr/bin/python3
"""Defines a file-appendining funcion."""


def append_write(filename="", text=""):
    """At the end of the UTF8 file append a string.

    Args:
        filename (str): Name of file to append.
        text (str): String to append.
    Returns:
        Number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
