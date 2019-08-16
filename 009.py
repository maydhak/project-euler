"""
Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""

"""
Before writing the solution, here is what I came up with:

Known equations/inequalities:
1) a + b + c = 1000 (problem statement)
2) a^2 + b^2 = c^2 (definition of Pythagorean triplet)
3) a + b > c (definition of a triangle)
4) a < b < c (problem statement)

Therefore,
c = 1000-a-b, so a+b > 1000-a-b. Then 
2a+2b > 1000, so a+b > 500 and c < 500.
"""

def solution9():
    for c in reversed(range(1, 500)):  # c < 500
        for a in range(1, 1000-c):  # the max value of a is 500 since b > 0
            if a**2 + (1000-c-a)**2 == c**2:  # b = (1000-c-a) since a + b + c = 1000
                return a*(1000-c-a)*c, a, (1000-c-a), c
                # first return value is the product, followed by the values of a, b, c

print(solution9())