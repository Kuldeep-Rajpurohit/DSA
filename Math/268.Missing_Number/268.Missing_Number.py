class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        fact = (n*(n+1))/2
        return (fact - sum(nums))
