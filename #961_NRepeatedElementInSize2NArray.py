class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        sum1 = sum(nums)
        sum2 = sum(set(nums))
        return (sum1 - sum2) // (n - 1)