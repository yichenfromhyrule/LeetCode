class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        result = 0
        while 5**i<=n:
            result+=n//(5**i)
            i+=1
        return result

if __name__ == '__main__':
    s = Solution()
    n = 30
    r = s.trailingZeroes(n)
    print(r)