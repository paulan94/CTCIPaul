import copy
def rot(grid):
    min_count = 0
    while True:
        grid_copy = copy.deepcopy(grid)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    for inc in (-1,1):
                        if r+inc >= 0 and r+inc < len(grid):
                            if grid[r+inc][c] == 1:
                                grid[r+inc][c] = 3
                        if c+inc >= 0 and c+inc < len(grid[0]):
                            if grid[r][c+inc] == 1:
                                grid[r][c+inc] = 3
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 3:
                    grid[r][c] = 2
        if grid == grid_copy:
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1:
                        return -1
            return min_count
        min_count += 1

grid = [[2,1,1],[1,1,0],[0,1,1]]

print (rot(grid))
