#!/usr/bin/python3
"""
Validation file
"""

def decimalToBinary(n):
    return "{0:b}".format(int(n))


def validUTF8(data):
    """check list of integer"""

    for i in data:
        binary = int(decimalToBinary(i))

        if binary > 99999999:
            return False
    
    return True
