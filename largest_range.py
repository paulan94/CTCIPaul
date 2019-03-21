def largestRange(array):
    # Write your code here.
    cur_big, cur_small = 0, 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            flag = True
            if array[i] > array[j]:
                small,big = array[j], array[i]
            else:
                small,big = array[i], array[j]
            for k in range(small,big+1):
                if not k in array:
                    flag = False
                    break
            if flag:
                if big - small > cur_big - cur_small:
                    cur_big, cur_small = big, small
    return [cur_small, cur_big]


print (largestRange([1,11,3,0,15,5,2,4,10,7,12,6]))
