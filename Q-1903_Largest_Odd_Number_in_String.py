class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """

        for i in range(len(num), 0, -1):
            if int(num[i-1]) % 2 == 1:
                return num[:i]
        else: return ""