class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort();
        s.sort();
        # Go through from the child with smallest g
        count = 0
        for child in g:
            while len(s) > 0 and s[0] < child:
                s.pop(0)
            if len(s) > 0:
                count += 1
                s.pop(0)
            else:
                return count
        return count
