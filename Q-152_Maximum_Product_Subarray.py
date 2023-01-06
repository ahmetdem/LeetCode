class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
            
        res = max(nums)
        currMax, currMin = 1, 1
        
        for n in nums:
            
            temp = currMax*n
            currMax = max(n, currMax*n, currMin*n)
            currMin = min(n, temp, currMin*n)
            res = max(res, currMax)
        
        return res