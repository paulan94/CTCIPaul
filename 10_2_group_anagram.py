from collections import defaultdict
def group_anagrams(str_arr):
    ana_dict = defaultdict(list)
    for word in str_arr:
        ana_dict[str(sorted(word))].append(word)

    idx = 0
    for vals in ana_dict.values():
        for val in vals:
            str_arr[idx] = val
            idx += 1


arr = ["cat", "ih", "hi", "act", "yo"]
print (arr)
group_anagrams(arr)
print (arr)
