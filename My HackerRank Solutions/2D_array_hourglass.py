#Paul An hackerrank 2d array DS problem

import sys

def main(arr):
    #replace arr values with i,j
    i,j = 0,0

    x1 = arr[i][j]
    x2 = arr[i][j+1]
    x3 = arr[i][j+2]

    x5 = arr[i+1][j+1]

    x7 = arr[i+2][j]
    x8 = arr[i+2][j+1]
    x9 = arr[i+2][j+2]

    hglass_val = x1+x2+x3+x5+x7+x8+x9

    max_hglass = hglass_val

    while i <= 3:
        while j <= 3:
            x1 = arr[i][j]
            x2 = arr[i][j+1]
            x3 = arr[i][j+2]

            x5 = arr[i+1][j+1]

            x7 = arr[i+2][j]
            x8 = arr[i+2][j+1]
            x9 = arr[i+2][j+2]

            hglass_val = x1+x2+x3+x5+x7+x8+x9

            #if the current hourglass is higher than the previous max, update the max to be the current hglass
            if hglass_val > max_hglass:
                max_hglass = hglass_val

            j += 1
        #reset j values, increment i
        j = 0
        i += 1

    return max_hglass



arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
answer = main(arr)

print answer


