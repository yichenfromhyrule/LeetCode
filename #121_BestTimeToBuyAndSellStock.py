class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        else:
            dp=[]
            if len(prices)==2:
                profit = prices[1]-prices[0]
                return profit if profit>0 else 0
            else:
                profit = prices[1] - prices[0]
                dp.append(profit)
                maxProfit = profit
                maxProfitIndex = 0
                for i in range(2, len(prices)):
                    print("current maxIndex=%d, maxProfit=%d, prices[%d]-prices[%d]=%d, prices[%d]-prices[%d]=%d."%(maxProfitIndex,dp[len(dp)-1],i,i-1,prices[i]-prices[i-1],i, maxProfitIndex,prices[i]-prices[maxProfitIndex]))
                    profit = max(dp[len(dp)-1],prices[i]-prices[i-1],prices[i]-prices[maxProfitIndex])
                    dp.append(profit)
                    if profit>=maxProfit:
                        maxProfit = profit
                        if profit==prices[i]-prices[i-1]:
                            maxProfitIndex = i-1 if prices[i-1]<prices[maxProfitIndex] else maxProfitIndex
                    print(dp)
            return maxProfit if maxProfit>0 else 0




if __name__ == '__main__':
    s = Solution()
    nums = [2,7,1,4,11]
    r = s.maxProfit(nums)
    print(r)