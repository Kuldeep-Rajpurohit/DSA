class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        rever = []
        for word in s:
            rever.append(word[::-1])
        return ' '.join(rever)
