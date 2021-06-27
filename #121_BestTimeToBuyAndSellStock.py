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
            profit = prices[1] - prices[0]
            dp.append(profit)
            maxProfit = profit
            left_index = 0
            min_value = 0 if prices[0]<=prices[1] else 1
            if len(prices)==2:
                return maxProfit if maxProfit>0 else 0
            else:
                for i in range(2, len(prices)):
                    min_value = i if prices[i]<prices[min_value] else min_value
                    print("current left Index=%d, maxProfit at this point =%d, prices[%d]-prices[%d]=%d, prices[%d]-prices[%d]=%d. prices[%d]-min value %d= %d"\
                          %(left_index,dp[len(dp)-1],i,i-1,prices[i]-prices[i-1],i, left_index,prices[i]-prices[left_index], i,min_value, prices[i]-prices[min_value]))
                    profit = max(dp[len(dp)-1],prices[i]-prices[i-1],prices[i]-prices[min_value])
                    dp.append(profit)
                    if profit>=maxProfit:
                        maxProfit = profit
                        if profit==prices[i]-prices[min_value]:
                            left_index = min_value if prices[min_value]<prices[left_index] else left_index
                    print(dp)
            return maxProfit if maxProfit>0 else 0




if __name__ == '__main__':
    s = Solution()
    nums = [2,1,2,1,0,1,2]
    r = s.maxProfit(nums)
    print(r)