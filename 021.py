"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair; each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math


def d(num):
    factors = set()
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:  # this is a divisor; its pair will also be added
            factors.add(i)
            if i != num / i:  # if this factor is the square root of the number, it shouldn't be double-counted
                factors.add(int(num/i))
    if num != 1:
        factors.remove(num)  # the number itself should be excluded
    return sum(factors)


def solution21(limit):
    # Returns the sum of all amicable numbers under limit
    # Idea for future improvement: add a dictionary that keeps track of a and d(a) already
    # then take b and just look up d(b) if it already exists; otherwise compute it
    amicable_nums = set()
    for a in range(1, limit+1):
        b = d(a)
        print("a = {} and b = {}".format(a, b))
        if a != b:
            if d(b) == a and b < limit:
                print(a, b)
                amicable_nums.add(a)
                amicable_nums.add(b)

    return sum(amicable_nums)


print(solution21(10000))
