class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = [nums[0]]
        for i in range(1, len(nums)):
            if i == 1:
                curr_max = max(nums[i], max_value[-1])
            else:
                if i-3 >= 0:
                    curr_max = max(max_value[i-2], max_value[i-3]) + nums[i]
                else:
                    curr_max = max_value[i-2] + nums[i]
            max_value.append(max(max_value[-1], curr_max))
        return max_value[-1]