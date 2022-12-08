class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def getDig(num):
            diglist = []
            
            while num > 0:
                lastDig = num % 10
                diglist.append(lastDig)
                num //= 10
            
            return diglist


        def isSelf(num):
            digitlist = getDig(num)
            if 0 in digitlist:
                return False
            for i in digitlist:
                if num % i != 0:
                    break
            else: return True 

        sequence = list(range(left, right+1))

        return list(filter(isSelf, sequence))