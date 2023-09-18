class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            dig = 0
            while n:
                n = n // 10
                dig += 1
            if dig %2 == 0:
                count += 1
        return(count)
        
