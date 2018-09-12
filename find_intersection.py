# Enter your code here. Read input from STDIN. Print output to STDOUT
#Find the intersection of two sorted integer arrays.
# [1,3,6,17,21], [2,4,6,21] # returns (6, 21)
# Are there duplicates in the arrays? Yes
# How do we handle duplicates in the array? For example, if we have [0, 1, 3, 3, 3, 4] and [2, 3, 3, 5] does this return (3), or (3, 3) or (3, 3, 3)
# We consider a number being in the intersection as “using” elements in the array. So we would return (3, 3).
# How big can the arrays be?
# You can assume that we can load the arrays into memory. We won’t be using streams
A = [1,3,6,17,21]
B = [2,4,6,21]

C =[0, 1, 3, 3, 3, 4]
D =[2,3,3,5]

#time: O(A+B), where A and B are lengths of the 2 arrays.
#space O(N), where n is the number of intersecting items.
def find_intersection(A,B): #took 5~ minutes to write
    intersection = []
    i,j = 0,0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] > B[j]:
            j += 1
        elif A[i] < B[j]:
            i += 1
    
    return intersection

    
print (find_intersection(A,B))
print (find_intersection(C,D))
