#!/usr/bin/python3
"""Defines the text file reading function."""


def read_file(filename=""):
    """Print to stdout the contents of a UTF8 text file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
