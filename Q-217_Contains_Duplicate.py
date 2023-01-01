class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hashMap = set()

        for num in nums: 
            if num in hashMap:
                return True
            hashMap.add(num)
        return False