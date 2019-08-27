"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import itertools


def solution24(lower, upper, perm_number):
    # Returns the perm_number-th lexicographic permutation of the digits ranging from lower to upper
    position = 0
    for perm in itertools.permutations(range(lower, upper+1)):
        position += 1
        if position == perm_number:
            return int("".join(str(digit) for digit in perm))


print(solution24(0, 9, 1000000))
