"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


import math


def facsum(num):
    facsum_result = 0
    for char in str(num):
        facsum_result += math.factorial(int(char))
    return facsum_result


def solution34():
    # If the number has 7 digits, the factorials of the digits could still add to get a 7-digit answer
    # But the sum of the factorials of the digits of the highest 8-digit number (99999999) is only 7 digits long
    # So the upper limit on the loop is 99999999. 1 and 2 are excluded by definition in the problem statement
    # also it's pretty obvious that none of the single-digit numbers will meet the criteria
    total = 0
    for i in range(11, 100000000):
        if facsum(i) == i:
            total += i
    return total


print(solution34())  # Answer: 40730
