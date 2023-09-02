class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

# Approarch 3 : Hashmap or dict
        d = {}
        for i in nums:
            if i in d:
                return(True)
            else:
                d[i] = True
        return(False)


# Approarch 2 : sort and check        

        # nums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return(True)
        # return(False)

# Approarch 1 : iterate through all the elements
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return(True)
        # return(False)
