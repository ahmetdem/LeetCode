class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        lenght, temp = 0, 0
        i = 0

        if len(s) == 1:
            return 1

        while i <= len(s):
            res = ""
            for l in s[i:]:   
                
                if l not in res:
                    res += l
                    continue

                break
            
            lenght = len(res)
            if lenght > temp:
                temp = lenght

            i += 1
        
        return temp
