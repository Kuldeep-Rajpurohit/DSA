class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pre, curr = cost[0], cost[1]
        for i in range(2, len(cost)):
            pre, curr = curr, min(pre, curr) + cost[i]
        return min(pre, curr)
