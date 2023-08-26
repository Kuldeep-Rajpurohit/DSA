class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        i = len(matrix)-1
        while i>0:
            j = 0
            while j<len((matrix[0]))-1:
                if matrix[i-1][j]== matrix[i][j+1]:
                    j+=1
                else:
                    return False
            i-=1
        return True
