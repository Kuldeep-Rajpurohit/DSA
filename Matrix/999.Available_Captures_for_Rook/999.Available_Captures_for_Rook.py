class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        horizontal = []
        vertical = []
        for i in range(0,8):
            temp_hor = ''
            temp_ver = ''
            for j in range(0,8):
                if board[i][j] != '.':
                    temp_hor = temp_hor + board[i][j]
                if board[j][i] != '.':
                    temp_ver = temp_ver + board[j][i]
            horizontal.append(temp_hor)
            vertical.append(temp_ver)
        count = 0
        new = horizontal + vertical
        for i in range(0,len(new)):
            if 'Rp' in str(new[i]):
                count +=1
            if 'pR' in str(new[i]):
                count +=1
        return(count)
