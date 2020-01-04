'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top
to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                            75
                          95 64
                        17 47 82
                      18 35 87 10
                    20 04 82 47 65
                  19 01 23 75 03 34
                88 02 77 73 07 63 67
              99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

small_triangle = '''3
4 7
8 4 2
3 9 5 8'''

big_triangle = '''75
                         95 64
                        17 47 82
                      18 35 87 10
                    20 04 82 47 65
                  19 01 23 75 03 34
                88 02 77 73 07 63 67
              99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


def parse_rows(triangle):
    # Splits the triangle into its rows
    rows = triangle.split("\n")
    return rows


def create_matrix(rows):
    # Creates a matrix (list of lists) where each list is a row, elements of the list are values in the row
    matrix = []
    for row in rows:
        matrix.append(row.lstrip().split(" "))
    return matrix


class Cell(object):
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = int(value)
        self.max_sum = 0
        self.max_side = None  # Used if you care about the path you took to reach the sum
        # Otherwise the side is not needed for this problem
    def __repr__(self):
        return "({}, {}, {})".format(self.value, self.max_sum, self.max_side)


def create_expanded_matrix(matrix):
    # Creates a Cell object at each location in the matrix
    for row in matrix:
        cellrow = matrix.index(row)
        for col in row:
            cellcol = row.index(col)
            matrix[cellrow][cellcol] = Cell(cellrow, cellcol, matrix[cellrow][cellcol])
    for cell in matrix[-1]:  # last row of the matrix
        # the max_sum if including that cell is that cell's value because nothing is below it
        # the default side is to the left (arbitrary)
        cell.max_sum = cell.value
        cell.max_side = 'l'
    return matrix


def pick_path(cell, matrix):  # cell is a Cell object, matrix holds all Cell objects
    # Establishes the max_sum when going down a path with that cell and the side to go to for it
    left = matrix[cell.row + 1][cell.col]
    right = matrix[cell.row + 1][cell.col + 1]
    if cell.value + left.max_sum > cell.value + right.max_sum:
        cell.max_sum = cell.value + left.max_sum
        cell.max_side = 'l'
    else:
        cell.max_sum = cell.value + right.max_sum
        cell.max_side = 'r'


def solution18(triangle):
    # set up the matrix from the triangle
    rows = parse_rows(triangle)
    matrix = create_matrix(rows)
    real_matrix = create_expanded_matrix(matrix)

    # find the best path - start with the second to last row and work backwards
    for row in reversed(real_matrix[:-1]):
        for cell in row:
            pick_path(cell, real_matrix)
    return real_matrix[0][0].max_sum

print(solution18(big_triangle))
