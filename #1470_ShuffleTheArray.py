class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        mid = len(nums)//2
        result = []
        for a,b in zip(nums[:mid], nums[mid:]):
            result += [a,b]
        return result