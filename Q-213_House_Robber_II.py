class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def house(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(nums[0], house(nums[:-1]), house(nums[1:]))
