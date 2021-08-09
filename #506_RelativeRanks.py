class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        score_copy = copy.deepcopy(score)
        score_copy.sort(reverse=True)
        hashmap = {}
        for i in range(len(score_copy)):
            hashmap[score_copy[i]] = i + 1
        result = []
        for s in score:
            if hashmap[s] == 1:
                result.append("Gold Medal")
            elif hashmap[s] == 2:
                result.append("Silver Medal")
            elif hashmap[s] == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(hashmap[s]))
        return result
