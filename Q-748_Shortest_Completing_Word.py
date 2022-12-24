import string
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate = licensePlate.lower()
        data = {}
        letters = {}
        
        for letter in licensePlate:
            if letter in string.ascii_lowercase:
                if letter in letters:
                    letters[letter] += 1
                else: 
                    letters[letter] = 1

        for word in words:
            if word not in data:
                data[word] = {}
            for letter in word:
                if letter in data[word]:
                    data[word][letter] += 1
                else:
                    data[word][letter] = 1

        

        check = []
        for word in words:
            if all(key in data[word] and data[word][key] >= value for key, value in letters.items()):
                check.append(word)
        else: 
            lenghts = [len(s) for s in check]
            return check[lenghts.index(min(lenghts))]