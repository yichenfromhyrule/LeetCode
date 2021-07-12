class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n >= 2:
            return self.isPowerOfTwo(n / 2.0)
        return True if n == 1 else False

if __name__ == '__main__':
    s = Solution()
    n = 13
    r = s.isPowerOfTwo(n)
    print(r)