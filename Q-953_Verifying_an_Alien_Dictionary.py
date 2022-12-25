from functools import cmp_to_key
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def compare_words(s1, s2):
            for c1, c2 in zip(s1, s2):
                c1_index = order.index(c1)
                c2_index = order.index(c2)

                if c1_index != c2_index:
                    return c1_index - c2_index


            return len(s1) - len(s2)

        # Use the comparison function to sort the list of words
        sorted_words = sorted(words, key=cmp_to_key(compare_words))


        return sorted_words == words
    
    
    
    
    
    
    
    
    
    
    
    