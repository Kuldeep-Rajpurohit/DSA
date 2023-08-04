class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for a in A:
            if A.count(a)>1:
                return(a)
