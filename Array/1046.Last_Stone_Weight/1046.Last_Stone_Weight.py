class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)>1:
            stones.sort()
            new = stones.pop(-1)-stones.pop(-1)
            if new:
                stones.append(new)
        if len(stones):
            return stones[-1]
        else:
            return 0
