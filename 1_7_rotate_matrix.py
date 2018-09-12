
matx = [[1,0,1,1], [1,1,1,1], [0,0,0,0],
        [1,0,0,1], [0,1,0,1], [1,1,1,1],
        [1,0,0,0], [1,1,0,0], [0,1,1,1]]

#rotate 90 degrees

def rotate_90(matx, n):
    big_n = n*n
    new_matx = []
    for i in range(n):
        idx = big_n - n + i
        while idx >= 0:
            new_matx.append(matx[idx])
            idx -= n

    return new_matx

x = rotate_90(matx,3)

for i in x:
    print (i)
