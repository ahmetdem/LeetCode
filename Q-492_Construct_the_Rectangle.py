import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """

        if area == 1:
            return [1,1]
        
        dif1 = area+1
        l1, w1 = 0,0
        
        for w in range(int(math.sqrt(area)), 0, -1):
            l = area//w
            
            if l*w == area:    
                l = area//w
            else: continue
            
            dif = abs(l - w)
            print(l, w, dif, dif1)

            if dif1 <= dif:
                return l1, w1
            else: dif1 = dif
            
            l1, w1 = l, w
        else: return l1, w1
        