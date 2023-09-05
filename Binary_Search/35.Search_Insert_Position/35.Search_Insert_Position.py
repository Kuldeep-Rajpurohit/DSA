class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        i = 0
        while nums[i] < target:
            i += 1
            if i == len(nums):
                break
        return i
