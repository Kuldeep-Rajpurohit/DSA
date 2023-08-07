class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        new = list(heights)
        new.sort()
        for i in range(0,len(new)):
            if new[i] != heights[i]:
                count += 1
        return(count)
