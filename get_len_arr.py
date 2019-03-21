#  Given a list of n words, the task is to check if two same words come next to each other.
#  Then remove the pair and print the number of words left in the list after this pairwise 
#  removal is done until no other pairs are present.
#  
#  Examples:
#  
#  Input : [ba bb bb bcd xy]
#  Output : 3
#  As [bb, bb] cancel each other so, [ba bcd xy] is the new list.
#  
#  Input :  [laurel hardy hardy laurel]


#  Output : 0
#  As first both [hardy] will cancel each other.
#  Then the list will be [laurel, laurel] which also remove
#  each other. So, the final list doesn't contain any
#  word.

#assumptions: can be more than 1 pair, new pairs can come from deletions of pairs
def get_len_arr(arr):
    stack = []

    if len(arr) <= 1: return len(arr)
    for ele in arr:
        if len(stack) == 0:
            stack.append(ele)
        else:
            popped = stack.pop()
            if ele != popped:
                stack.append(popped)
                stack.append(ele)

    return len(stack)


a = ['laurel', 'hardy', 'hardy', 'laurel']
a2 = ['bc', 'bb', 'bb', 'bcd', 'xy']



print (get_len_arr(a))

print (get_len_arr(a2))
