class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        numList = []
        
        
        #get the list of numbers smaller than n
        for i in range(1, n+1):
            numList.append(i)
        
        #check if the conditions hold, if it is then replace the words 
        for i in numList:
            index = i-1
            
            if i % 3 == 0 and i % 5 == 0:
                numList[index] = "FizzBuzz"
            elif i % 3 == 0:
                numList[index] = "Fizz"
            elif i % 5 == 0:
                numList[index] = "Buzz"
        
        
        for i in range(len(numList)):
            numList[i] = str(numList[i])
            
        return numList