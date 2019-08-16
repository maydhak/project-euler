"""
Problem 4:
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
# I wrote my own method for checking if a number is a palindrome. I thought that the number should read the same
# from the start to its middle digit, and from the end to its middle digit in reverse, so that's what my function checks.
# Later I learned that there are much more concise ways to do this... but anyways...

def solution4():
    def is_palindrome(num):
        import math
        work = str(num)
        half = int(math.ceil((len(work)/2)))
        return work[:half-1] == ''.join(reversed(work[half:])) or work[:half] == ''.join(reversed(work[half:]))

    num1, num2, soln = 999, 999, 0
    for i in reversed(range(num1)):
        for j in reversed(range(num2)):
            if is_palindrome(i*j) and i*j > soln:
                soln = i*j
    print(soln)

# After reading about strides at https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
# I wrote a better version of is_palindrome.

def new_is_palindrome(num):
    return str(num) == str(num)[::-1]

# At this point I didn't even need the palindrome checker to be in its own function, so I rewrote the solution:

def solution4_1():
    num1, num2, soln = 999, 999, 0
    for i in reversed(range(100, num1)):
        for j in reversed(range(100, num2)):
        # I also realized that only three-digit numbers needed to be included, so I added that in the range calls
            if str(i*j) == str(i*j)[::-1] and i*j > soln:
                soln = i*j
    print(soln)