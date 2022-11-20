class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        def sumDigits(num):
            lastDigit = 0
            global sum
            sum = 0
            
            digitLen = len(str(num))
            
            for i in range(digitLen):
                lastDigit = num % 10
                num = num // 10
                sum = sum + lastDigit
            return sum
                
        while True:
            
            sumDigits(num)
            if sum < 10:
                return sum
                break
            else:
                num = sum 