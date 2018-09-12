from collections import defaultdict
def check_perm_palindrome(some_str):
    if not some_str: return None
    if len(some_str) == 0: return True
    char_dict = defaultdict(int) #def val for key set to 0.

    for char in some_str:
        if char_dict[char] > 0:	char_dict[char] -= 1
        elif char_dict[char] == 0: char_dict[char] += 1

    if len(some_str) % 2 == 0:
        return sum(char_dict.values()) == 0
    else: #in the case it’s odd.
        return sum(char_dict.values()) == 1

print (check_perm_palindrome("tactcoa"))
