class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        for op in ops:
            m = op[0] if op[0] < m else m
            n = op[1] if op[1] < n else n
        return m * n