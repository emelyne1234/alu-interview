#!/usr/bin/python3
""" number of units of water retained by the walls"""


def rain(walls):
    if len(walls) == 0:
        return 0
    n = len(walls)
    left = 0
    right = n-1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if walls[left] < walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                water = water + left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]

            else:
                water = water + right_max - walls[right]

            right -= 1

    return water
