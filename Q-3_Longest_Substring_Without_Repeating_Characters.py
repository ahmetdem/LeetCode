class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        lenght, temp = 0, 0
        i = 0
        res = ""

        if len(s) == 1:
            return 1 

            
        while i <= len(s):
            for l in s[i+len(res):]:   
                if l not in res:
                    res += l
                    lenght = len(res)
                    continue
                
                res = res.replace(res[0], "")
                break
                    
            if lenght > temp:
                temp = lenght

            i += 1
                   
        return temp
