#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    """Perform a magic calculation based on the values of a and b."""
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
