
from collections import defaultdict
def getMaxOccurrences(s, minLength, maxLength, maxUnique):
    # Write your code here
    count_occ = 0
    i,j = 0, minLength-1
    while len(s[i:j+1]) <= maxLength and j < len(s)+1:
        while j < len(s)+1:
            if len(s[i:j+1]) <= maxLength:
                #check how many unique occurrences
                # if str_look has <= maxUnique count instances
                sub_s = s[i:j+1]
                sub_count = count_unique(sub_s)
                print (sub_s, sub_count)
                if sub_count <= maxUnique and sub_count > count_occ:
                    count_occ = sub_count
            j += 1
        i += 1
        j = i + minLength
    return count_occ
        
def count_unique(some_str):
    count_dict = defaultdict(int)
    for c in some_str:
        count_dict[c] += 1
    return max(count_dict.values())


print (getMaxOccurrences("abcde",2,4,5))
