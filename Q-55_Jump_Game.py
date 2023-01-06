class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return True 

        last = len(nums) - 1
        first = len(nums) - 2
        isit = False
        
        for i in range(len(nums)-1):
            
            if nums[first] >= (last - first):
                last = first
                isit = True
            else: isit = False       
            first -= 1 
                        
        return isit