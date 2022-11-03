class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        listLen = len(num)
        number = 0
        
        
        for i in num:
            listLen -= 1
            number = number + i * 10**listLen
            
        number += k
        
        result = list(str(number))
        
        return result
