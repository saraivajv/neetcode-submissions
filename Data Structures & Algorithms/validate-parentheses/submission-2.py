class Solution:
    def isValid(self, s: str) -> bool:
        valid_chars = {')': '(', '}': '{', ']': '['}
        char_stack = []
        for char in s:
            if char in valid_chars:
                if char_stack and char_stack[-1] == valid_chars[char]:
                    char_stack.pop()
                else:
                    return False
            else:
                char_stack.append(char)
        if not char_stack :
            return True 
        else:
            return False

