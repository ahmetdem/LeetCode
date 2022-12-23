class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        try:
            return [i for i in range(1,n+2) if n % i == 0][k-1]
        except:
            return -1