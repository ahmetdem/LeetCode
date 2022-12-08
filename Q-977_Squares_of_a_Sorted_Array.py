class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = [x*x for x in nums]
        res.sort()

        return res