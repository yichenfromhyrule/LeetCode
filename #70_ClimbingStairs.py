class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(0, n+1)]
        dp[0] = 1
        dp[1] = 1
        if n>1:
            for i in range (2, n+1):
                dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

if __name__ == '__main__':
    s = Solution()
    n = 7
    r = s.climbStairs(n)
    print(r)