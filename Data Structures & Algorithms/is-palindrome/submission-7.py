class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l].isalnum() == False:
                l += 1
            while r > l and s[r].isalnum() == False:
                r -= 1
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        