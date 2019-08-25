"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def solution25():
    a, b = 1, 1
    index = 2  # this index refers to b
    while b < 10**999:  # 10^1 has two digits, 10^2 has three digits, so 1000 digits means 10^999
        a, b = b, a+b
        index += 1
    return index


print(solution25())
