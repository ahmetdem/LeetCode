class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
            
        t = [0, 1, 1]
    
        for i in range(n - 2):
            t.append(sum(t))
            t.pop(0)
        
        return t[-1]   
        
