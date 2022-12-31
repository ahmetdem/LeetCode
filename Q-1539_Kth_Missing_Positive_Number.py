class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        return [i for i in range(1, k+1+len(arr)) if i not in arr][k-1]