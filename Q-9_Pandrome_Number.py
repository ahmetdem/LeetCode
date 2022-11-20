class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        
        """
        
        originalNum = x 
        # reverse the given number
        reverse_num = 0
        while x > 0:
            reminder = x % 10
            reverse_num = (reverse_num * 10) + reminder
            x = x // 10

                
        if originalNum == reverse_num:
            return True 
        else:
            return False
            