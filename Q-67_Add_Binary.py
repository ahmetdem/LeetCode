class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        intA = int(a, 2)
        intB = int(b, 2)
        
        total = intA + intB
        
        binTotal = bin(total)
        binTotal = binTotal[2:]
        
        return str(binTotal)