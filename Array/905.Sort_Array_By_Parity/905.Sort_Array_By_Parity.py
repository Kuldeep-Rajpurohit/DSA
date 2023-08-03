class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        C = []
        for a in (A):
            if a%2==0:
                B.append(a)
            else:
                C.append(a)
        return(B+C)
