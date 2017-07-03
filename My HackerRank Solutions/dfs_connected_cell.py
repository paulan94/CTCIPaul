#Paul An
'''Given an nxm matrix, find and print the number of cells in the largest region in the matrix.
 Note that there may be more than one region in the matrix.'''
def get_biggest_region(grid):
    biggest_region = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            biggest_region = max(biggest_region, get_adjacent_count(grid, i, j))
    return biggest_region


def get_adjacent_count(grid, i, j):
    if not (i in range(len(grid)) and j in range(len(grid[0]))):
        return 0
    if (grid[i][j] == 0):
        return 0
    count = 1
    grid[i][j] = 0
    count += get_adjacent_count(grid, i + 1, j + 1)
    count += get_adjacent_count(grid, i + 1, j - 1)
    count += get_adjacent_count(grid, i + 1, j)
    count += get_adjacent_count(grid, i - 1, j)
    count += get_adjacent_count(grid, i - 1, j + 1)
    count += get_adjacent_count(grid, i - 1, j - 1)
    count += get_adjacent_count(grid, i, j - 1)
    count += get_adjacent_count(grid, i, j + 1)
    return count


n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
