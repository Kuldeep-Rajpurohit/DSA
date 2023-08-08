class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = nums
        new.sort()
        sum = 0
        for i in range(0, len(new), 2):
            sum += new[i]
        return sum
        
