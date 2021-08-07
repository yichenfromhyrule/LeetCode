class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_length = 0
        result_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                result_length = max(result_length, curr_length)
                curr_length = 0
            else:
                curr_length += 1
        return max(result_length, curr_length)