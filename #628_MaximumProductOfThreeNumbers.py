class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        else:
            nums.sort()
            # if all are positive
            if nums[0] >= 0:
                return nums[-1] * nums[-2] * nums[-3]
            else:
                return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])