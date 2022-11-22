class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 0: return 1
        
        elif n > 0:
            return x ** n
        
        else: return (1/x) ** -n