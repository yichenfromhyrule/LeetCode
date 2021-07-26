class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        news = ""
        for c in s:
            news += str(ord(c) - 96)
        while k > 0:
            r = 0
            for newc in news:
                r += int(newc)
            news = str(r)
            k -= 1
        return r
