from collections import defaultdict
def group_anagrams(arr):
    for idx in range(len(arr)):
        for jdx in range(idx+1, len(arr)):
            tmp = arr[idx+1]
            if isAnagram(arr[jdx],arr[idx]):
                arr[idx+1] = arr[jdx]
                arr[jdx] = tmp
                         


def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = defaultdict(int)
        for c in s:
            s_map[c] += 1
        for c in t:
            s_map[c] -= 1
        for val in s_map.values():
            if val != 0:
                return False
        return True


s = ["cat", "move", "tac", "hello", "ey", "what", "act", "ye"]

group_anagrams(s)
print (s)
