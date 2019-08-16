"""
Problem 15:
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# Answer based off of https://betterexplained.com/articles/navigate-a-grid-using-combinations-and-permutations/
# Works for a square grid of grid_size

def solution15(grid_size):
    path_length = grid_size*2
    routes = 1
    while path_length > grid_size:  # generating all routes
        routes *= path_length
        path_length -= 1
    while grid_size >= 1:  # removing redundancies
        routes /= grid_size
        grid_size -= 1
    print(int(routes))