class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left, right = 0,len(seats)
        left = seats.index(1)
        rev = seats[::-1]
        right = rev.index(1)
        count = 0
        midd = 0
        for i in range(left, len(seats)-right):
            if seats[i]==0:
                count+=1
            elif seats[i]==1:
                count = 0
            midd = max(midd, count)
        res = max(left, right, midd//2 if midd%2==0 else (midd+1)//2)
        return(res)
