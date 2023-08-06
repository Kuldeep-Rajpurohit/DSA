class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        allemails = set()
        for email in emails:
            left = email.split('@')[0]
            right = email.split('@')[1]
            left = left.split('+')[0]
            left = left.replace('.','')
            email = left + '@' +right
            allemails.add(email)
        return(len(allemails))
