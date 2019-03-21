def b_m(arr):
    candidate = 0
    count = 0
    for value in arr:
      if count == 0:
        candidate = value
      if candidate == value:
        count += 1
      else:
        count -= 1
      print (candidate,count)

a = [1,3,1,3,1,3,3,2,2,3,3] 

#bm checks if one element exists more than n//2 times. in arr. 
print (b_m(a))
