class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """

        for good in ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]:
            if good in num:
                return good
        else: return ""