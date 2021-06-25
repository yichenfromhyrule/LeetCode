class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        else:
            dp = [[-1 for i in range(len(prices))] for i in range(len(prices))]
            maxProfit = 0
            for i in range(0,len(prices)):
                for j in range(i+1,len(prices)):
                    currProfit=prices[j]-prices[i]
                    dp[i][j] = currProfit if currProfit>0 else -1
                    maxProfit = currProfit if currProfit > maxProfit else maxProfit
            return maxProfit


if __name__ == '__main__':
    s = Solution()
    nums = [7,6,4,3,1]
    r = s.maxProfit(nums)
    print(r)