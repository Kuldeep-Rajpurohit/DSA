class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            copy, new = x , 0
            while copy:
                new = new * 10 + copy % 10
                copy = copy // 10
            return x == new
        
