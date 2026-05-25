class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0
        dicts = set()
        for r in range(len(s)):
            while s[r] in dicts:
                dicts.remove(s[l])
                l += 1
            dicts.add(s[r])
            count = max(count, len(dicts))
        return count
