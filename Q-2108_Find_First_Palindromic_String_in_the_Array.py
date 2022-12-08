class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        """

        def isPalindrome(word):
            check = word[::-1]
            if word == check:
                return True 
            else: return False

        for word in words:
            if isPalindrome(word):
                return word
        else: return ""
