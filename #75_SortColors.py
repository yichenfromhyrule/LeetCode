class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        num1 = 0
        num2 = 0
        for j in range(len(nums)):
            if nums[j] == 2:
                num2 += 1
            elif nums[j] == 1:
                num1 += 1
            else:
                nums[i] = 0
                i += 1
        for index1 in range(i,i+num1):
            nums[index1] = 1
        for index2 in range(i+num1, i+num1+num2):
            nums[index2] = 2