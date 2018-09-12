def sparse_search(arr,start,end,x):
    if end < start: return None
    else:
        mid = (start+end)//2
        if arr[mid] == x:
            return mid
        if arr[mid] == "":
            left = mid-1
            right = mid+1
##            print ("l {} r {}".format(left,right))
            while arr[left] == "" and arr[right] == "" and left >= 0 and right <len(arr):
                left -= 1
                right += 1
            if arr[left] == x: return left
            if arr[right] == x: return right
            if arr[left] != "" and arr[left] > x:
                return sparse_search(arr, start, left-1,x)
            elif arr[left] != "" and arr[left] < x:
                return sparse_search(arr,left+1,end,x)

            if arr[right] != "" and arr[right] > x:
                return sparse_search(arr, start, right-1,x)
            elif arr[right] != "" and arr[right] < x:
                return sparse_search(arr,right+1,end,x)
        elif arr[mid] < x:
            return sparse_search(arr,mid+1,end,x)
        elif arr[mid] > x:
            return sparse_search(arr,start,mid-1,x)
        


inp = ["at","","","","ball","","","car","", "","dad","",""]

print (sparse_search(inp,0,len(inp)-1,"ball"))
