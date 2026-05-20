class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            m = (bot + top) // 2 # middle row value
            if target < matrix[m][0]:
                bot = m - 1
            elif target > matrix[m][-1]:
                top = m + 1
            else:
                break
        
        if not (top <= bot):
            return False
        l, r = 0, len(matrix[m]) - 1
        while l <= r:
            middle_value = (r + l) // 2 # middle value from M row
            if target < matrix[m][middle_value]:
                r = middle_value - 1
            elif target > matrix[m][middle_value]:
                l = middle_value + 1
            else:
                return True
        return False
