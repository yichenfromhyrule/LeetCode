class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        can_or_not = [0 for n in range(len(nums))]
        max_target = 0
        for i in range(0, len(nums)-1):
            if i <= max_target:
                can_or_not[i] = i+nums[i]
                max_target = max(max_target, can_or_not[i])
        return max_target >= len(nums)-1