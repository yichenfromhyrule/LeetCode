class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 1
        start = 0
        end = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[end]:
                end += 1
            else:
                max_length = max(max_length, end-start+1)
                start = i
                end = i
        return max(max_length, end-start+1)