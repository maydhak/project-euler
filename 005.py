"""
Problem 5:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def solution5(mynum):
    # Returns the smallest positive number that is evenly divisible by all numbers from 1 to mynum
    from functools import reduce

    def lcm(num, nums_found):
        current_lcm = reduce(lambda x, y: x*y, nums_found)
        if current_lcm % num != 0:  # No need to multiply further if the current LCM already divides the number
            current_lcm *= num
            nums_found.append(num)

            # This part divides out the GCF of the new number and the previous LCM
            highest_factor = 1
            for possible_factor in range(1, num):
                if num % possible_factor == 0:
                    highest_factor = possible_factor
            current_lcm /= highest_factor
            if highest_factor != 1:
                nums_found.remove(highest_factor)

        return reduce(lambda x, y: x*y, nums_found), nums_found
        # nums_found might have changed so the reduce function has to be called again on it to return the LCM

    result_nums = [1]
    for i in range(1, mynum):
        result_nums = lcm(i, result_nums)[1]  # pass the updated list of factors to the next number

    return lcm(mynum, result_nums)[0]


print(solution5(20))
