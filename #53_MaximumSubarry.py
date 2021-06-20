class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp
        dp = [0 for i in range(len(nums))]
        #l = 0
        #r = 0
        if len(nums)==1:
            return nums[0]
        else:
            dp[0] = nums[0]
            max_sum = nums[0]
            for i in range (1, len(nums)):
                if dp[i-1] + nums[i]>nums[i]:
                    #r = i
                    dp[i] = dp[i-1]+nums[i]
                else:
                    #l = i
                    dp[i] = nums[i]
                if dp[i]>max_sum:
                    max_sum=dp[i]

        return max_sum



if __name__ == '__main__':
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    r = s.maxSubArray(nums)
    print(r)