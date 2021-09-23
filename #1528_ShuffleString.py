class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        l = []
        for c, i in zip(s, indices):
            l.append((i,c))
        l.sort()
        r = ""
        for m in l:
            r += m[1]
        return r