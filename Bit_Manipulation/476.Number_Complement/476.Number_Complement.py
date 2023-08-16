class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = ''
        new = str(bin(num))
        new = new.split('b')[1]
        comp = len(new)*'1'
        ans = int(new)+int(comp)
        ans = str(ans)
        ans = ans.replace('2','0')
        my = int(ans,2)
        return(my)
