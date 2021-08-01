class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        rotate = k % len(nums)
        lastpart = nums[:len(nums)-rotate]
        for i in range(0, rotate):
            nums[i] = nums[len(nums)-rotate+i]
        m = 0
        for j in range(rotate, len(nums)):
            nums[j] = lastpart[m]
            m += 1