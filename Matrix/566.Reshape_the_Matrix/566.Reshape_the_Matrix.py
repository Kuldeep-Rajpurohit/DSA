class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        new = [[]]
        if len(nums)* len(nums[0]) != r*c:
            return nums
        k = 0
        for row in nums:
            for ele in row:
                if k<c:
                    new[-1].append(ele)
                else:
                    new.append([ele])
                    k=0
                k+=1
        return new
