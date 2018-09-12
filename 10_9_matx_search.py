
def matrix_search(matx, target, row_start, row_end, col_start, col_end):
    if not matx or row_start > row_end or col_start > col_end:
        return None
    else:
        row_mid = (row_start + row_end)//2
        col_mid = (col_start + col_end)//2

        if matx[row_mid][col_mid] == target:
            return row_mid, col_mid

        elif matx[row_mid][col_mid] < target:
            col_search = matrix_search(matx,target,row_start,row_end,
                                       col_mid+1, col_end)
            row_search = matrix_search(matx,target,row_mid+1,row_end,
                                       col_start, col_end)
            return col_search or row_search
        
        elif matx[row_mid][col_mid] > target:
            col_search = matrix_search(matx,target,row_start,row_end,
                                       col_start, col_mid-1)
            row_search = matrix_search(matx,target,row_start,row_mid-1,
                                       col_start, col_end)

            return col_search or row_search


matx = [[15,20,30,45],
        [20,25,35,50],
        [35,40,45,60],
        [50,55,60,65]]


print (matrix_search(matx,65,0,3,0,3))
