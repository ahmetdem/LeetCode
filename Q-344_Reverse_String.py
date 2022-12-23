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
    