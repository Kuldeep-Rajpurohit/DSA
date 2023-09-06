class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        while l != 0:
            temp = s.pop(l - 1)
            s.append(temp)
            l -= 1
