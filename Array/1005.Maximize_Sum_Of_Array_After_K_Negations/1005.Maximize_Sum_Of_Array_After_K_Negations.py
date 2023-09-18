class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A = sorted(A)
        i = 0
        while K > 0 and A[i] < 0:
            A[i] = abs(A[i])
            i += 1
            K -= 1
        if K == 0 or K % 2 == 0 or 0 in A:
            return sum(A)
        else:
            return(sum(A) - 2*min(A))
