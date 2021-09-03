class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        start = 0 if nums[0]==0 else 1
        result = [1] if nums[0]==0 else [0]
        for i in range(1, len(nums)):
            start += start if nums[i]==0 else (start + 1)
            result += [1] if start % 5 == 0 else [0]
        return result