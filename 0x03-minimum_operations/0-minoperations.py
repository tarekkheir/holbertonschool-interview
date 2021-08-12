#!/usr/bin/python3
"""
Minimum operations module
"""


def minOperations(n):

    result = 0
    denom = 2

    while n >= 2:

        if n % denom != 0:
            denom += 1
        else:
            n = n / denom
            result = result + denom

    return result
