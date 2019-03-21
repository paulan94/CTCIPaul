##def binSearch(arr,x):
##    start, end = 0, len(arr)-1
##    mid = (start+end)//2
##    if (x == arr[mid]):
##        return True
##    while (start < end):
##        if (x > arr[mid]):
##            return binSearch(arr[mid+1:], x)
##        elif (x < arr[mid]):
##            return binSearch(arr[:mid],x)
##    return False

def binarysearch(start,end,arr,key):
    mid = 1+(end-start)//2
    while mid > -1:
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binarysearch(start,mid-1,arr,key)
        elif arr[mid] < key:
            return binarysearch(mid+1,end,arr,key)
    return -999

a = [2,6,13,21,36,47,63,81,97]

##print (binSearch(a,48))
print (binarysearch(0,len(a)-1,a,81))
