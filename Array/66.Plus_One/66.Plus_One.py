class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        l = len(digits)
        for i in range(0,l):
            string += str(digits.pop(0))
        ans = 1+ int(string)
        ans = str(ans)
        res = list(map(int, str(ans)))
        return(res)
