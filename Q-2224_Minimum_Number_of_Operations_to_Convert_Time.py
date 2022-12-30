class Solution(object):
    def convertTime(self, current, correct):
        """
        :type current: str
        :type correct: str
        :rtype: int
        """

        def toMin(time):
            time = time.split(":")
            time = [int(time) for time in time]
            
            return time[0]*60 + time[1]

        valid = [60,15,5,1]
        time = toMin(current)
        i = 0
        check = 0

        while time != toMin(correct):
            
            if time + valid[i] > toMin(correct):
                i += 1
            else:
                time += valid[i]
                check += 1
            
        return check
    
    
    
    