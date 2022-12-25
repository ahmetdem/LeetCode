class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        l1 = s1.split(" ")
        l2 = s2.split(" ")

        return [word for word in l1 if word not in l2 and l1.count(word) == 1] + [word for word in l2 if word not in l1 and l2.count(word) == 1]
            
    