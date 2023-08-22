class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num = 0
        for i in range(len(A)):
            num = num*10 + A[i]
        return (list(map(int, str(num+K))))
