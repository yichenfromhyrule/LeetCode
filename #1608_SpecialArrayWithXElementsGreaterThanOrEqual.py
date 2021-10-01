class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums.sort()
        for i in range(l, 0, -1):
            if nums[l - i] >= i:
                if (l - i - 1) >= 0:
                    if nums[l - i - 1] < i:
                        return i
                else:
                    return i
        return -1
