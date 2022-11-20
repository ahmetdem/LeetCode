class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        sList = s.split(" ")
        
        for i in range(len(sList)):
            print()
            if sList.count("") == 0:
                break
            sList.remove("")
        
        
        lastWord = sList[-1]
        
        return len(lastWord)
