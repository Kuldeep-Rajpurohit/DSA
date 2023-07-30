class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = str(x)
        rev = ''
        j = 0
        if x == 0:
            return('0')
        if x >=(2**31)-1 or x<=(-2**31):
            return('0')
        else:
            if x > 0:
                rev = n[::-1]
            else:
                strg = n[:0:-1]
                rev =strg
        for i in range(0,len(rev)):
            if rev[i]!='0':
                break
            j = j+1
        final = rev[j:]
        if x<0:
            final = '-'+final
        if int(final) >=(2**31)-1 or int(final)<=(-2**31):
            return('0')
        return(final)
