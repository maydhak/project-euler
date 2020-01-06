'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.
'''


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


def solution67(triangle):
    # set up the matrix from the triangle
    rows = parse_rows(triangle)
    matrix = create_matrix(rows)
    real_matrix = create_expanded_matrix(matrix)

    # find the best path - start with the second to last row and work backwards
    for row in reversed(real_matrix[:-1]):
        for cell in row:
            pick_path(cell, real_matrix)
    return real_matrix[0][0].max_sum


big_triangle = open("067_triangle.txt").read()
print(solution67(big_triangle))
