class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        o = []
        string = str(A[0])
        for e in string:
            flag = 0
            for i in range(1,len(A)):
                if e in str(A[i]):
                    left, right = A[i].split(e,1)
                    A[i] = left + right
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                o.append(e)
        return o
    
