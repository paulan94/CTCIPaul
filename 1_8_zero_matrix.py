matx = [[0,1,1,1],
        [1,1,1,0],
        [1,1,1,1],
        [1,1,1,1]]

def zero_matrix(grid):
    rows = len(grid)
    cols = len(grid[0])

    copy_matx = [[0,1,1,1],
        [1,1,1,0],
        [1,1,1,1],
        [1,1,1,1]]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                zero_copy(copy_matx,r,c)
    grid = copy_matx

    return grid

    

def zero_copy(copy_matx,r,c):
    rows = len(copy_matx)
    cols = len(copy_matx[0])
    for rw in range(rows):
        copy_matx[rw][c] = 0
    for cl in range(cols):
        copy_matx[r][cl] = 0
        

##def zero_matrix(matx):
##    new_matx = matx[:]
##    rows,cols = len(matx), len(matx[0])
##    for i in range(rows):
##        for j in range(cols):
##            if matx[i][j] == 0:
##                zero_row(i, new_matx)
##                zero_col(j, new_matx)
##    return new_matx
##
##def zero_row(row, nmatx):
##    for i in range(len(nmatx)):
##        matx[row][i] = 0
##
##def zero_col(col, nmatx):
##    for i in range(len(nmatx[0])):
##        nmatx[i][col] = 0
##        
for i in (zero_matrix(matx)):
    print (i)
