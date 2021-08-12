class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        curr_sum = sum(list(set(nums)))
        correct_sum = (1 + len(nums)) * len(nums) * 0.5
        lost_item = correct_sum - curr_sum
        dupl_item = sum(nums) + lost_item - correct_sum
        return [int(dupl_item), int(lost_item)]
