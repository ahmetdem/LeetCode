class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        

        def base(num, base):
            numbers = []
            while num > 0: 
                numbers.append(num % base)
                num //= base
            
            
            return sum(numbers)

        return base(n, k)