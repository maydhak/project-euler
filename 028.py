"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

"""
Logic: By drawing an 11 x 11 spiral I noticed that the numbers on the diagonals could be obtained by adding even numbers 
(2, 4, 6, etc) in sets of 4 (so four increases of 2, then four increases of 4, then four increases of 6, and so on). 
The code generates the numbers on the diagonals in this way (the largest number will be the size of the spiral, squared) 
and then adds all the numbers up. 
"""


def solution28(size):
    # Finds the sum of the numbers on the diagonals of a size by size spiral formed by starting with 1
    # and moving to the right in a clockwise direction
    diagonal_nums = {1}
    num = 1
    incrementer = 2
    while num < size**2:
        counter = 4
        while counter > 0:
            num += incrementer
            diagonal_nums.add(num)
            counter -= 1
        incrementer += 2

    return sum(diagonal_nums)


print(solution28(1001))
