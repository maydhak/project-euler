"""
Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def solution3():
    quo = 600851475143
    factors = set()
    divisor = 2
    while quo > 1:
        if quo % divisor == 0:
            factors.add(divisor)
            quo /= divisor
        else:
            divisor += 1
            # only increment the divisor if it did not divide in; else we want to start over at 2 for the new quotient
    return max(factors)


print(solution3())
