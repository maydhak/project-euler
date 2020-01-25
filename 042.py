"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

How many of the words in words.txt are are triangle words?
"""

import string


def solution42(file_name):
    word_values = []
    for word in open(file_name).read().split(","):
        word_value = 0
        for letter in word:
            word_value += string.ascii_uppercase.find(letter) + 1
        word_values.append(word_value)

    #  Only need to generate the triangular numbers that are less than or equal to the max word_value
    triangle_nums = {0}
    n = 1
    while max(triangle_nums) <= max(word_values):
        triangle_nums.add(int(0.5*n*(n+1)))
        n += 1

    # The word values have already been calculated so now we just need to check which ones are triangular
    total = 0
    for word_value in word_values:
        if word_value in triangle_nums:
            total += 1

    return total


filename = "042_words.txt"
print(solution42(filename))  # Answer: 162
