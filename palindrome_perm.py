#Paul An
#CTCI 1.4 Palindrome Permutation

#first attempt, needs same # of letters if even,
#or only one word can be unique if odd # of numbers

from collections import defaultdict

def main(word_to_check):
    word_to_check = word_to_check.replace(' ','')
    word_dict = defaultdict(int)
    for char in word_to_check:
        word_dict[char] += 1
    if len(word_to_check) % 2 == 0: #if even, check to see if values are even, if not return false
        for v in word_dict.values():
            if v % 2 != 0:
                return False
    else: #if odd, only one value must be odd
        odd_counter = 0
        for v in word_dict.values():
            if v % 2 != 0:
                odd_counter += 1
        if odd_counter > 1:
            return False
        else:
            return True

if __name__ == "__main__":
     print (main('taco cat'))
    
