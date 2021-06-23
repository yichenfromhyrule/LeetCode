class Solution(object):
    def sortPrices(self, prices, sortedList, start, end):
        currentPrices = prices[start:end+1]
        if len(currentPrices)==1:
            sortedList.append(currentPrices)
        else:
            mid = (start+end)//2

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==1:
            return 0
        else:
            return 1







if __name__ == '__main__':
    s = Solution()
    nums = [7,2,5,3,10,4,0,9]
    r = s.maxProfit(nums)
    print(r)