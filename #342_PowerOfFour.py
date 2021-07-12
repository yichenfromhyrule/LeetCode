class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n >= 4:
            return self.isPowerOfFour(n / 4.0)
        return True if n == 1 else False