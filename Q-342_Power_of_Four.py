class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        
        
        if n == 0: return False
        elif n < 0: return False
        else:
            x = math.log(n, 4)
            x = round(x, 9)
            if x % 1 == 0: return True
            else: return False
