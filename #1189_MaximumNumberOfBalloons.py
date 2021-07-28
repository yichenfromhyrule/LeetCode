class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        ban_list = {'b': 0, 'a': 0, 'n': 0}
        lo_list = {'l': 0, 'o': 0}
        for c in text:
            if c in ban_list:
                ban_list[c] += 1
            elif c in lo_list:
                lo_list[c] += 1
        return min(min(list(lo_list.values())) // 2, min(list(ban_list.values())))
