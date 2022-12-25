class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n % 2 == 1:
            return "".join("a"*n)
        else: return "".join("a"*(n-1)) + "b"