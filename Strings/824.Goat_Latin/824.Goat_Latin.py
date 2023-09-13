class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = list(S.split(' '))
        j = 2
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(0, len(S)):
            if S[i][0] in vowels:
                S[i] = str(S[i]) + 'm' + 'a'*j
                j += 1
                flag = 1
            else:
                S[i] = S[i][1:] + S[i][0] + 'm' + 'a'*j
                j += 1
        return " ".join(S)
