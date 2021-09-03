class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        result = 0
        for x, y in zip(heights, expected):
            if x!=y:
                result += 1
        return result