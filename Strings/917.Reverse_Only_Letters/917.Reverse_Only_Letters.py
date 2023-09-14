class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        new = ''
        symb = []
        for i in range(0, len(S)):
            if S[i].isalpha():
                new = new + S[i]
            else:
                symb.append([i, S[i]])
        new = new[::-1]
        for i in range(0,len(symb)):
            new = new[:symb[i][0]] + symb[i][1] + new[symb[i][0]:]
        return new
