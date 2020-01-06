"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

from functools import reduce


def solution40():
    num = "".join(str(i) for i in range(1, 1000000))  # will produce a number with enough digits
    digits = [int(num[0]), int(num[9]), int(num[99]), int(num[999]), int(num[9999]), int(num[99999]), int(num[999999])]
    return reduce(lambda a, b: a*b, digits)


print(solution40())  # Answer: 210
