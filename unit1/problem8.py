# Write a function local_maximums() that accepts an n x n integer matrix grid and returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:
# local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
# In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

def local_maximums(grid):
    n = len(grid)
    output_size = n - 2
    output = [[0] * output_size for _ in range(output_size)]

    for i in range(output_size):
        for j in range(output_size):
            max_val = float('-inf')
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    max_val = max(max_val, grid[r][c])
            output[i][j] = max_val

    return output

grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
print(local_maximums(grid))

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
print(local_maximums(grid))