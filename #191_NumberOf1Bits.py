class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            a = n >> 1
            a <<= 1
            if n - a == 1:
                count += 1
            n>>=1
        return count