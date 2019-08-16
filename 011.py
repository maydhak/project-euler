"""
Problem 11:
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
up, down, left, right, or diagonally) in the 20×20 grid?
"""

grid = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

def assign_space(grid):
    # Create a mapping of every grid space (numbered 1-400 left to right, top to bottom) and the number in that space
    return_dict = {}
    counter = 1
    nums = grid.replace("\n", " ").split(" ")
    for num in nums:
        return_dict[str(counter)] = num
        counter += 1
    return return_dict

gridded = assign_space(grid)  # Store the mapping in a variable

def multiply(start_num, end_num, interval):
    # Multiplies all of the numbers in a set of 4; returns the spaces/numbers in the set and the product
    possible_combo = {}
    combo_product = 1
    for num in range(start_num, end_num+1, interval):
        combo_product *= int(gridded[str(num)])
        possible_combo[str(num)] = gridded[str(num)]
    return (possible_combo, combo_product)

def check_max(possible_combo, combo_product, max_combo, max_product):
    # Checks if the product of the possible set of 4 is larger than the largest one found so far; returns the highest combo/product
    if combo_product > max_product:
        max_combo = possible_combo
        max_product = combo_product
    return (max_combo, max_product)

def increase_func(start, end, max_combo_parameter, max_product_parameter, regular_increase, regular_check, next_row_increase, interval):
    """
    Traverses the grid to find all combinations in a certain direction and identify the largest product in that direction
    :param start: the starting space number of a combination
    :param end: the ending space number of a combination
    :param max_combo_parameter: holds the spaces and numbers that make up the combo with the largest product
    :param max_product_parameter: value of the largest product
    :param regular_increase: how much to increase the space numbers by if a border has not been reached
    :param regular_check: if this condition is met, the combination spaces will continue to be traversed horizontally,
    except for vertical combinations, in which case they will continue to be traversed vertically.
    :param next_row_increase: how much to increment the space by if a border of the grid has been reached
    :param interval: used by the 'multiply' function to pull the correct spaces from the grid to be multiplied.
    For any combination type, the 'difference' in space numbers is the same for all numbers in the combination.
    For horizontal combinations, the difference is 1 (ie spaces 1, 2, 3, 4 make up a combo)
    For vertical combinations, the difference is 20 (ie spaces 1, 21, 41, 61 make up a combo)
    For left downward diagonal combinations, the difference is 19 (ie spaces 4, 23, 42, 61 make up a combo)
    For right downward diagonal combinations, the difference is 21 (ie spaces 1, 22, 43, 64 make up a combo)
    :return: the maximum product of the combination and the spaces/numbers that were multiplied
    """

    start_num = start
    end_num = end
    max_combo = max_combo_parameter
    max_product = max_product_parameter
    while True:
        increase = regular_increase if eval(regular_check) else next_row_increase
        start_num += increase
        end_num += increase
        if end_num > 400:
            break

        possible_result = multiply(start_num, end_num, interval)
        checked = check_max(possible_result[0], possible_result[1], max_combo, max_product)
        max_combo = checked[0]
        max_product = checked[1]

    return(max_combo, max_product)


result1 = increase_func(0, 3, {}, 1, 1, "start_num % 20 < 18", 4, 1)  # All horizontal combinations
result2 = increase_func(-19, 41, result1[0], result1[1], 20, "start_num < 341", -319, 20)  # All vertical combinations
result3 = increase_func(0, 57, result2[0], result2[1], 1, "start_num % 20 != 0", 4, 19)  # All combinations going diagonally leftward down
result4 = increase_func(-3, 60, result3[0], result3[1], 1, "end_num % 20 != 0", 4, 21)  # All combinations going diagonally rightward down

print("The maximum product is " + str((result4)[1]))
print(result4[0].values())
