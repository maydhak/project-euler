"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def solution20(num):
    # Finds the sum of digits in the number num!
    result = 1
    while num > 1:
        result *= num
        num -= 1
    sum = 0
    for digit in str(result):
        sum += int(digit)
    return sum

print(solution20(100))