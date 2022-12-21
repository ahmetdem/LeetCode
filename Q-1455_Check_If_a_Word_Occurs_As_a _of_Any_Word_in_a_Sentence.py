class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """

        def isTrue(sentence, searchWord):
            value = 0
            for word in sentence.split():
                value += 1
                if searchWord in word:
                    if atStart(word, searchWord):
                        return value
            else: return -1

        def atStart(word, searchWord):
            word = word[:len(searchWord)]
            if word == searchWord:
                return True
            else: return False
        
        return isTrue(sentence, searchWord)