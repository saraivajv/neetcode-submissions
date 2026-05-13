class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        max_char = max(len(s), len(t))
        char_set = dict()

        for i in range(max_char):
            if i < len(s):
                char_set[s[i]] = char_set.get(s[i], 0) + 1
            if i < len(t):
                char_set[t[i]] = char_set.get(t[i], 0) - 1
        print(char_set)
        for val in char_set.values():
            if val != 0:
                return False
        return True