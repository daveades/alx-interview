#!/usr/bin/python3

"""
Implementation of pascal's triangle
"""


def pascal_triangle(n):
    """
    Given a non-negative integer n, generate the first n rows of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
