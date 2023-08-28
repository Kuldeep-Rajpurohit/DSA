class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        A = [1]
        for i in range(1,rowIndex+1):
            A = [1] + [A[i]+A[i-1] for i in range(1,len(A))] + [1]
        return A
