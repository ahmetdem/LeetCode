class Solution(object):
    import math 
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        guess = 1.0
        while abs(guess*guess - x) > 0.5:
            guess = (guess + x/guess)/2
        return int(math.floor(guess))
