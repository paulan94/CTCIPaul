import operator
grid = [[5, 7, 8, 6, 3],
         [0, 0, 7, 0, 4],
         [4, 6, 3, 4, 9],
         [3, 1, 0, 5, 8]]


def hungry_rabbit(grid):# -> number of carrots eaten
    #should find center of grid with most carrots
    #recursive function to check which adjacent cell has the most carrots
    center_points = find_center(grid)
    starting_point = choose_center(grid,center_points)
    
    start_row = starting_point[0]
    start_col = starting_point[1]
    
    carrots_start = grid[start_row][start_col]

    visited = set()
    visited.add((start_row,start_col))
    
    carrot_count = eat_carrots(grid,start_row, start_col, visited)
    carrots_eaten = carrots_start
    for r,c in carrot_count:
        carrots_eaten += grid[r][c]
    return carrots_eaten


def find_center(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    center_points = []
    #handle if grid is 2x2 or less
    center_row = num_rows//2
    center_col = num_cols//2
    if (num_rows * num_cols) % 2 == 1: # odd means there is a center
        center_points.append([center_row, center_col])
    else:
        #if even, check which row or col is odd
        if num_rows % 2 == 1: #rows is odd, cols is even
            for itv in [-1,0]:
                center_points.append([center_row, center_col+itv])
        elif num_cols % 2 == 1: #cols is odd, rows even
            for itv in [-1,0]:
                center_points.append([center_row+itv, center_col])
        else: #both are even
            for itv in [-1,0]:
                for itv2 in [-1,0]:
                    center_points.append([center_row+itv, center_col+itv2])
##    print (center_points)
    return center_points

def choose_center(grid, center_points):
    highest = grid[center_points[0][0]][center_points[0][1]]
    cur_cell = (center_points[0][0],center_points[0][1])
    for row,col in center_points[1:]:
        if grid[row][col] > highest:
            cur_cell = (row,col)
    return cur_cell


def eat_carrots(grid, row_start,col_start,visited=set(), path = []):
    #should be simple dfs...
    if row_start < 0 or col_start < 0 or row_start > len(grid)-1 or col_start > len(grid[0])-1:
        return 0
    if not grid[row_start][col_start]:
        return 0
    potential_cells = dict()
    for itv in [-1,1]:
        if (row_start + itv) >= 0 and (row_start + itv) < len(grid)-1 and (row_start+itv, col_start) not in visited and grid[row_start+itv][col_start] > 0:
            potential_cells[(row_start+itv, col_start)] = grid[row_start + itv][col_start]
    for itv in [-1,1]:
        if (col_start + itv) >= 0 and (col_start + itv) < len(grid)-1 and (row_start, col_start+itv) not in visited and grid[row_start][col_start+itv] > 0:
            potential_cells[(row_start, col_start+itv)] = grid[row_start][col_start+itv]
    if len(potential_cells.items()) > 0:
        highest = max(potential_cells.items(), key=operator.itemgetter(1))[0]
        visited.add((highest[0], highest[1]))
        path.append(highest)
        eat_carrots(grid,highest[0], highest[1],visited, path)
    return path
    
##def eat_carrots(grid, row_start, col_start, carrots_eaten, visited= set()):
##    if row_start < 0 or col_start < 0 or row_start > len(grid)-1 or col_start > len(grid[0])-1:
##        return 0
##    if not grid[row_start][col_start]:
##        return 0
##    else:
##        potential_cells = dict()
##        
##        for itv in [-1,1]:
##            if (row_start + itv) >= 0 and (row_start + itv) < len(grid)-1:
##                potential_cells[(row_start+itv, col_start)] = grid[row_start + itv][col_start]
##        for itv in [-1,1]:
##            if (col_start + itv) >= 0 and (col_start + itv) < len(grid)-1:
##                potential_cells[(row_start, col_start+itv)] = grid[row_start][col_start+itv]
##        if (row_start, col_start) in visited:
##            #should remove that cell from list to check, but ran out of time!
##            return 0
##        highest = max(potential_cells.items(), key=operator.itemgetter(1))[0]
##        print (highest)
##        carrots_eaten += grid[highest[0]][highest[1]]
##        visited.add((highest[0],highest[1]))
##        eat_carrots(grid,highest[0], highest[1], carrots_eaten, visited)
##        return carrots_eaten
        

print(hungry_rabbit(grid)) # should be 27
    
