class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        else:
            result = x
            negative = False
            if n < 0:
                negative = True
            n = abs(n)
            while n > 1:
                result *= x
                n -= 1
            return 1/result if negative else result

if __name__ == '__main__':
    s = Solution()
    x = 2.00000
    n = 10
    r = s.myPow(x,n)
    print(r)