# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         c = nums.count(val)
#         i = 0
#         while c != 0:
#             if nums[i] == val:
#                 nums.pop(i)
#                 c -= 1
#             else:
#                 i += 1
#         return len(nums)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2:
            if nums[p2] == val:
                p2 -= 1
            elif nums[p1]  == val:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1
        return(p2+1)
