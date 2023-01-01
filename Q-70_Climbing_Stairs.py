class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        hashMap = [0,1,1]
        
        if n == 1:
            return 1
            
        for i in range(n-1):    
            
            hashMap[0] = hashMap[1] + hashMap[2]
            hashMap[2] = hashMap[1]
            hashMap[1] = hashMap[0]
            
        return hashMap[0]
