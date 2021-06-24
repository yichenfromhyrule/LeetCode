class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        else:
            left = 0
            right = len(prices)-1
            profit = prices[right]-prices[left]
            while left<right:
                curr_profit = prices[right]-prices[left]
                if curr_profit<profit:
                    

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,6,5,0,3]
    r = s.maxProfit(nums)
    print(r)