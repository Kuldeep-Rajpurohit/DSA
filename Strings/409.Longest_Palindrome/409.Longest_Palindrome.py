class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = flag = c = 0
        for r in set(s):
            c = s.count(r)
            if c%2==0:
                count += c
            elif c%2!=0:
                count += c-1
            if flag == 0 and c%2!=0:
                count+=1
                flag=1
        return count
