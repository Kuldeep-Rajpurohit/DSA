class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        new = list(sorted(nums))
        return new[len(new)//2]
