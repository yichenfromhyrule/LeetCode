class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        for i in range(2, len(nums)):
            if nums[i-2] < nums[i-1] + nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        return 0