#!/usr/bin/python3
"""Defines Pascal's triangle function."""


def pascal_triangle(n):
    """Representing Pascal's triangle of n size."""

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trigl = triangles[-1]
        temp = [1]
        for i in range(len(trigl) - 1):
            temp.append(trigl[1] + trigl[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
