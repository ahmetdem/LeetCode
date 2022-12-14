class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        counter = {}

        for n in nums1:
            if n in counter:
                counter[n] += 1
            else: counter[n] = 1


        result = []
        for num in nums2: 
            if num in counter and counter[num] > 0:
                result.append(num)
                counter[num] -= 1 #most important part

        return result