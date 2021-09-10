class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        r = n // 2
        result = []
        for i in range(1, r + 1):
            result += [i, (-1) * i]
        if n % 2 != 0:
            result += [0]
        return result

