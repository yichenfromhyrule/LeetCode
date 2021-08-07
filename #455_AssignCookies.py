class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        gpointer = 0
        spointer = 0
        result = 0
        while gpointer < len(g) and spointer < len(s):
            if s[spointer] >= g[gpointer]:
                result += 1
                gpointer += 1
            spointer += 1
        return result
