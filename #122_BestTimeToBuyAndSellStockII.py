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
            right = 1
            profit = prices[1]-prices[0]
            sum_profit = 0
            while right<len(prices):
                print("curr profit =%d is made by index%d - index%d, sum profit is %d" % (profit, right, left, sum_profit))
                if prices[right]<prices[right-1]:
                    print("A")
                    if left==right-1:
                        print("A1")
                        if len(prices) > right + 1:
                            left = right
                            right = right + 1
                        else:
                            return sum_profit
                    else:
                        print("A2")
                        for i in range(left+1, right-1):
                            currL_profit = prices[right-1]-prices[i]
                            if currL_profit>profit:
                                profit=currL_profit
                                left = i
                        if profit>0:
                            sum_profit+=profit
                        if len(prices)>right+1:
                            left = right
                            right = right+1
                            profit = prices[right]-prices[left]
                        else:
                            return sum_profit
                        right+=1
                else:
                    print("B")
                    currR_profit = prices[right]-prices[left]
                    if currR_profit>=profit:
                        print("B+1")
                        profit=currR_profit
                        right+=1
                        print("right =", right)


            for i in range(left + 1, right - 1):
                currL_profit = prices[right - 1] - prices[i]
                if currL_profit > profit:
                    profit = currL_profit
                    left = i
            if profit>0:
                sum_profit+=profit
            return sum_profit




if __name__ == '__main__':
    s = Solution()
    nums = [3,2,6,5,0,3]
    r = s.maxProfit(nums)
    print(r)