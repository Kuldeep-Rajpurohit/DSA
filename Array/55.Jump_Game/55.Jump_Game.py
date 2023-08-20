class Solution:
    def canJump(self, nums: List[int]) -> bool:
        new = 0
        if len(nums)==1:
            return(1==1)
        for i in range(0, len(nums) - 1):
            new = max(new, nums[i])
            if new == 0:
                return(1==0)
            if (new + i) >= (len(nums) - 1):
                return (new + i) >= (len(nums) - 1)
            
            new = new - 1
        return (1 == 0)
      
