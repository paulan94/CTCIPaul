def zero_matrix(grid): #- > None
    if not grid: return None
    new_matx = [[1,1,0],
     [1,1,1],
     [0,1,0]]
    print (new_matx)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                change_to_zero(row,col,new_matx)

    return new_matx

def change_to_zero(r,c,matx): #0,2
    for row in range(len(matx)):
        matx[row][c] = 0
    for col in range(len(matx[0])):
        matx[r][col] = 0

x = [[1,1,0],
     [1,1,1],
     [0,1,0]]

for i in zero_matrix(x):
    print (i)
