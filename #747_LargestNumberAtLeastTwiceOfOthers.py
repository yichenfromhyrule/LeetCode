class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        else:
            largest = 0
            for i in range(1, len(nums)):
                largest = i if nums[i] > nums[largest] else largest
            nums.sort()
            if nums[-1] >= 2*nums[-2]:
                return largest
            else:
                return -1