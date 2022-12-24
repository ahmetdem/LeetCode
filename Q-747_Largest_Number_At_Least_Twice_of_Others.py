class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = nums.index(max(nums)) 
        maxNum = nums.pop(nums.index(max(nums)))

        check = [i*2 for i in nums]
        check.append(max(nums))

        nums.insert(index, maxNum)

        if maxNum >= max(check):
            return nums.index(maxNum)
        else: return -1