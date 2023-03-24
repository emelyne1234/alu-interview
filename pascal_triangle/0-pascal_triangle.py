#!/usr/bin/python3
"""prints the triangle"""


def pascal_triangle(n):
    """prints it"""
    if n <= 0:
        return []
    triangle = [[1]]
    for x in range(1, n):
        row_previous = [0] + triangle[x - 1] + [0]
        row = [1]
        for y in range(0, len(row_previous) - 1):
            row.append(row_previous[y] + row_previous[y + 1])
            triangle.append(row)
    return triangle[:n]
