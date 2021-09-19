class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        r = [0] * (l - 1) + [sum(nums)]
        if l == 1:
            return r
        else:
            for i in range(l - 2, -1, -1):
                r[i] = r[i + 1] - nums[i + 1]
            return r
