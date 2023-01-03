class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        liste = [num for num in nums if num % 3 == 0 and num % 2 == 0]
        if len(liste) == 0:
            return 0

        return sum(liste)//len(liste)