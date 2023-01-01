class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        seq = [0, 1, 0]
    
        for i in range(n - 1):
            seq[2] = seq[1] + seq[0]
            seq[0] = seq[1]
            seq[1] = seq[2]
            
        return seq[2]