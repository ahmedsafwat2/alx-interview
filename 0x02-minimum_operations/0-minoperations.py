#!/usr/bin/python3
"""
In a text file, there is a single character H.
number of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """Calculate fewest no. of operations needed to result in n H characters"""
    t = 0
    m = 2
    while n > 1:
        while not n % m:
            t += m
            n /= m
        m += 1
    return t
