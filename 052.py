"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""


def digits(num):
    digits_in_num = []
    for digit in str(num):
        digits_in_num.append(digit)
    return digits_in_num


def solution52():
    found = False  # whether or not the number has been found
    x = 11  # I knew for sure the first few numbers weren't going to meet this criteria
    while not found:
        original_num_digits = digits(x)  # need to recalculate for each x
        for i in range(2, 7):
            num_to_check = x*i
            digits_to_check = digits(num_to_check)
            if not all(elem in original_num_digits for elem in digits_to_check):
                # this is where I learned the order of the lists matters!
                break
            if i == 6:  # successfully made it through the whole loop
                found = True
        x += 1

    return x-1  # will have added on an extra 1 at the end before breaking out of the loop
    # so we need to return 1 less than that


print(solution52())  # Answer: 142587
