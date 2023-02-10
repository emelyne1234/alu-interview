#!/usr/bin/python3
""" about minimum operations """


def minOperations(n):
    """determines the lowest number of operations"""
    operations = 0
    x = 2
    while n > 1:
        while n % x == 0:
            operations += 1
            n /= x
        x += 1
    return operations
