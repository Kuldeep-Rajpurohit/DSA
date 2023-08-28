class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        right_total = 0
        
        for i in range(len(nums)):
            right_total += nums[i]
        
        left_total = 0
        
        for i in range(len(nums)):
            if right_total-nums[i] == left_total:
                return(i)
            else:
                left_total += nums[i]
                right_total -= nums[i]
        
        return(-1)
