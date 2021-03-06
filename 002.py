"""
Problem 2:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""
# Done with help from https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence
# Because I wasn't sure how to generate a fibonacci sequence...

def solution2():
    a, b = 1, 2
    sum = 0
    while True:
        if b % 2 == 0 and b < (4000000):
            sum += b
        elif b > (4000000):
            break
        a, b = b, a+b
    print(sum)

# Revised solution after seeing https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p002.py:
# Oh wow, looks like we ended up doing the exact same thing in the end.

def solution2_1():
    a, b = 1, 2
    sum = 0
    while b < 4000000:
        if b % 2 == 0:
            sum += b
        a, b = b, a+b
    print(sum)