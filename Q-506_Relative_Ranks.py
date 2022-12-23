class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        sorted_score = list(reversed(sorted(score)))
        answer = []
        placement = {}

        for i in range(len(score)):
            placement[sorted_score[i]] = i

        for k in range(len(score)):
            if placement[score[k]] == 0:
                answer.append("Gold Medal")
            elif placement[score[k]] == 1:
                answer.append("Silver Medal")
            elif placement[score[k]] == 2:
                answer.append("Bronze Medal")
            else:
                answer.append(str(placement[score[k]]+1))
        
        else: return answer