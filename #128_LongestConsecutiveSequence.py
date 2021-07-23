class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        if len(nums) == 0:
            return 0
        else:
            curr_checking = nums[0]
            max_length = 1
            curr_length = 1
            for i in range(1, len(nums)):
                if nums[i] == curr_checking + 1:
                    curr_length += 1
                elif nums[i] == curr_checking:
                    curr_length += 0
                else:
                    max_length = max(max_length, curr_length)
                    curr_length = 1
                curr_checking = nums[i]
            return max(curr_length, max_length)
