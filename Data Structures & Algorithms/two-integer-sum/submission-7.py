class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existing_nums = {num: [] for num in nums}
        for i in range(len(nums)):
            existing_nums[nums[i]].append(i)
        for list_nums in existing_nums:
            if (target - list_nums) in existing_nums:
                if target - list_nums != list_nums:
                    return [existing_nums[list_nums][0], existing_nums[target - list_nums][0]]
                else:
                    if len(existing_nums[target - list_nums]) > 1:
                        return [existing_nums[list_nums][0], existing_nums[target - list_nums][1]]