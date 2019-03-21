def bin_search(arr,key,start,end):
    #we need to check if the end index is greater than 0 because
    #we need to ensure that end is within the bounds of [0:len(a)-1]
    if (start <= end):
        #mid will be start + (end-start)//2
        #the first start keeps track of where our lower bound is
        #and we move to the right (end-start)//2 times
        mid = start + (end-start)//2
        if (arr[mid] == key):
            return mid
        elif (arr[mid] > key):
            return bin_search(arr,key,start,mid-1)
        else:
            return bin_search(arr,key,mid+1,end)
    return -1

#  0 1 2 3 4  5
a=[2,5,7,9,11,20]

print (bin_search(a,20,0,len(a)-1))
##print (bin_search_iterative(a,9))
