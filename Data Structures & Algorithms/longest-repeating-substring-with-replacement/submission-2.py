class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = {}
        l = 0
        count = 0
        for r in range(len(s)):
            letters[s[r]] = 1 + letters.get(s[r], 0)
            if (r - l + 1) - max(letters.values()) > k:    
                letters[s[l]] -= 1
                l += 1
            count = max(count, r - l + 1)
        return count