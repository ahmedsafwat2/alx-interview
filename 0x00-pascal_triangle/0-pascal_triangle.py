#!/usr/bin/python3
"""
0-pascal_Rectangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for row in range(1, n):
        temp=[1]
        for col in range(row - 1):
            temp.append(k[row - 1][col] + k[row - 1][col + 1])
        temp.append(1)
        k.append(temp)
    return k
