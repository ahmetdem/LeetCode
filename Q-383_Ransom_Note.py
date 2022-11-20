class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        #make a list for both 
        rndNote = list(ransomNote)
        mgzn = list(magazine)
                
            
        #check in a loop if ransomlist letters are in magazine letters
        for i in mgzn:
            for j in rndNote:
                
                if i == j:
                    rndNote.remove(j)
            
        
        if len(rndNote) == 0:
            return True
        else:
            return False
    
        
        