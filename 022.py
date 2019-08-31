"""
names.txt is a 46K text file containing over five-thousand first names.
Begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import string


def solution22(filename):
    # Returns total scores of all names in a given file
    names_list = []
    for name_to_insert in open(filename).read().split(","):
        index = 0
        for name in names_list:
            if name_to_insert[1:-1] > name:
                index += 1
        names_list.insert(index, name_to_insert[1:-1])

    # function to multiply letters of the name by their score and return a score for the whole name
    def name_score_function(name, position):
        name_score = 0
        for letter in name:
            name_score += string.ascii_uppercase.find(letter) + 1
        name_score *= position
        return name_score

    total_name_scores = 0
    position_in_list = 1
    for name in names_list:
        total_name_scores += name_score_function(name, position_in_list)
        position_in_list += 1

    return total_name_scores


filename = "022_names.txt"
print(solution22(filename))
