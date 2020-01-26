"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def solution48():
    series = 0
    for i in range(1, 1001):
        series += i**i

    return int(str(series)[-10:])


print(solution48())  # Answer: 9110846700
