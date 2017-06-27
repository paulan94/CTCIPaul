#Hash Tables: Ransom Note
#Paul An

from collections import defaultdict
def ransom_note(magazine, ransom):
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word] += 1
    for word in ransom:
        if dicty[word] == 0: return False
        print word, "decrementing"
        dicty[word] -= 1
    return True

        # mag_list = []
        # rans_list = []
        # temp_list = []
        # for i in magazine:
        #     mag_list.append(i)
        # for j in ransom:
        #     rans_list.append(j)
        #     temp_list.append(j)
        # for ransom_word in rans_list:
        #     if ransom_word in mag_list:
        #         mag_list.remove(ransom_word)
        #         temp_list.remove(ransom_word)
        #
        # if len(temp_list) == 0:
        #     return True
        # else:
        #     return False



m, n = 6,4
magazine = "give me one grand today night".strip().split(' ')
ransom = "give me grand today".strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print "Yes"
else:
    print "No"

