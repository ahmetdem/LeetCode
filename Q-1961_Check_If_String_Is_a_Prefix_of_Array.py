class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        temp = ""
        for word in words:
            temp = temp + word
            
            if temp == s:
                return True 
        else: return False
