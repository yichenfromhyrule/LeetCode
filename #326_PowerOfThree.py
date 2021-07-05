class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n % 3 != 0 or n == 0:
            return False
        elif n / 3 == 1:
            return True
        else:
            return self.isPowerOfThree(n / 3)

if __name__ == '__main__':
    s = Solution()
    n = 28
    r= s.isPowerOfThree(n)
    print(r)