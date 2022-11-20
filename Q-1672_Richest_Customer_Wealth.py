class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        ans = 0
        
        for i in accounts:
            temp = sum(i)
            
            if temp > ans:
                ans = temp
                
        return ans