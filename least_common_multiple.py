"""
Write a function that calculates the least common multiple of its arguments; each argument is assumed to be a non-negative integer. In the case that there are no arguments (or the provided array in compiled languages is empty), return 1. If any argument is 0, return 0.

"""

from math import lcm

def lcm_of_args(*args):

    for number in args:
        if number == 0:
            return 0

    return lcm(*args) if not args is None else 1
