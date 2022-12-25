class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        
        return len([word for word in words1 if word in words2 and words1.count(word) == words2.count(word) == 1])