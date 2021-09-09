class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        string_nums = [len(str(n)) for n in nums]
        count = 0
        for s in string_nums:
            if s%2 == 0:
                count += 1
        return count