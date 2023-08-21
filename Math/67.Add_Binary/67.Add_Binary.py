class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = '0b' + a
        b = '0b' + b
        ans = int(a,2) + int(b,2)
        ans = str(bin(ans))
        return (ans.split('b')[1])
