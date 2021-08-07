class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        min_value = nums[0]
        nums = map(lambda x: x - min_value, nums)
        return sum(nums)

