class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc = dec = 0
        for i in range(1, len(A)):
            if A[i] - A[i - 1] > 0:
                inc = 1
            elif A[i] - A[i - 1] < 0:
                dec = 1
            if inc * dec == 1:
                return (False)
        return (True)
