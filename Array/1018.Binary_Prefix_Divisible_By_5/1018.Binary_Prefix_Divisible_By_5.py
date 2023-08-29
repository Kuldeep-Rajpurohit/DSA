class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        num = 0
        ans = []
        for i in range(len(A)):
            num = (num*2 + A[i]) % 5
            ans.append(num % 5 == 0)
        return ans
