class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        listLen = len(digits)
        number = 0
        
        
        for i in digits:
            listLen -= 1
            number = number + i * 10**listLen
        
        number += 1
        
        result = list(str(number))
        
        return result