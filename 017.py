"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

import math

nums_names_lengths = {
    1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3,
    11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8,  # these don't follow a pattern
    20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6,
    100: 10, 200: 10, 300: 12, 400: 11, 500: 11, 600: 10, 700: 12, 800: 12, 900: 11, 1000: 11
}


def num_name_length_counter(num):
    total = 0
    while num > 0:
        if num < 20:
            total += nums_names_lengths[num]
            num -= num
        elif num < 100:
            tens = math.floor(num/10)
            total += nums_names_lengths[tens*10]
            num -= tens*10
        else:
            # I grouped 1000 in here for the purposes of this problem since it is only going from 1-1000
            # otherwise, numbers 1000 and greater would have to be dealt with in another case.
            hundreds = math.floor(num/100)
            total += nums_names_lengths[hundreds*100]
            num -= hundreds*100
            if num != 0:
                total += 3  # for the 'and' in the number
    return total


def solution17(num):
    # Returns the number of letters used to write out all the numbers from 1 to num in words
    result = 0
    for i in range(1, num+1):
        result += num_name_length_counter(i)
    return result


print(solution17(1000))
