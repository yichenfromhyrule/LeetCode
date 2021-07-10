class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        negative = True if (divisor < 0 and dividend >= 0) or (divisor >= 0 and dividend < 0) else False
        divisor = abs(divisor)
        dividend = abs(dividend)
        while dividend >= divisor:
            dividend -= divisor
            result += 1
        return (0-result) if negative else result


if __name__ == '__main__':
    s = Solution()
    x = 10
    n = 3
    r = s.divide(x,n)
    print(r)