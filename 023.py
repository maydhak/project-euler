"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28
is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of
two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be
written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import math


def abundant(num):
    factors = set()
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            factors.add(i)
            factors.add(int(num/i))
    factors.remove(num)
    return sum(factors) > num


def solution23():
    abundant_numbers = set(i for i in range(12, 28124) if abundant(i))  # we know the smallest abundant number is 12

    # first identify all the sums of two abundant numbers
    sums = set()
    for i in abundant_numbers:
        for i2 in abundant_numbers:
            if i+i2 <= 28123:
                sums.add(i+i2)
            else:
                break  # no need to continue trying to make sums with numbers larger than this one

    # remove all the numbers between 1 and 28123 that are known sums of two abundant numbers
    nums_left = set(range(1, 28124))
    for number in sums:
        nums_left.remove(number)

    return sum(nums_left)  # add up the numbers that can't be made from the sum of two abundant numbers


print(solution23())
