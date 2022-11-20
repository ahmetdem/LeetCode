class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = str(s)
        
        s = s.lower()
        result = ''.join(filter(str.isalnum, s))
        
        check = result[::-1]
        
        if result == check:
            return True
        else:
            return False