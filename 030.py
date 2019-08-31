"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


"""
First I wrote a function to find the sum of the power-th power of a number's digits:
"""


def sum_of_powers(num, power_to_raise):
    total = 0
    for digit in str(num):
        total += int(digit)**power_to_raise
    return total


"""
When the number is small, it is smaller than the sum of the powers of its digits; but at some point the number itself 
exceeds the sum of the power of its digits. I needed to find the first suitably large number where the number is larger 
than the sum of its digits.  
Since the highest power-producing number is 9, I looked at numbers that only had digits of 9 in them: 9, 99, 999, etc. 
Basically I was looking for n such that (n*9^5) < (number with n digits of 9.)
"""

print(9, sum_of_powers(9, 5))
print(99, sum_of_powers(99, 5))
print(999, sum_of_powers(999, 5))
print(9999, sum_of_powers(9999, 5))
print(99999, sum_of_powers(99999, 5))
print(999999, sum_of_powers(999999, 5))
print(9999999, sum_of_powers(9999999, 5))
print(99999999, sum_of_powers(99999999, 5))

"""
Result:
9 59049
99 118098
999 177147
9999 236196
99999 295245
999999 354294 -- This is first time the number is greater than the sum of digits, and I took this as my upper bound.
9999999 413343
99999999 472392

Now I just had to loop over all the numbers to 999999, find the ones whose sum of digits equalled the number, add them
up and return the result. 
"""


def solution30():
    result_nums = set()
    for num in range(10, 1000000):  # start at 10 because single-digit numbers can't have 'sums' of their digits
        # and end at 1000000 because Python stops at 1 before the end of the range
        if num == sum_of_powers(num, 5):
            result_nums.add(num)
    return sum(result_nums)


print(solution30())
