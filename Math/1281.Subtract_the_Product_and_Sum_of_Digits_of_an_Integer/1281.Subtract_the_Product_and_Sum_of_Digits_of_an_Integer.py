class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pro, sum = 1, 0
        for dig in str(n):
            pro = pro*int(dig)
            sum += int(dig)
        return pro-sum
