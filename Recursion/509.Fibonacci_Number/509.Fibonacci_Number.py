class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0:
            return (0)
        if N==1:
            return(1)
    
        Num = [0, 1]
        count = 2
        while count < N:
            Num.append(Num[count-1] + Num[count-2])
            count += 1
        return (Num[N-1]+Num[N-2])
