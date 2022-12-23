class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        for i in range(len(s)):
            check = (len(s)-1)-i
            for j in range (check):
                s[j], s[j+1] = s[j+1], s[j]
                
        return s
    
    
        """
        def reverse_string(s):
            # Initialize left and right indices
            left = 0
            right = len(s) - 1

            # Swap elements until the indices meet in the middle
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1 
        """
    