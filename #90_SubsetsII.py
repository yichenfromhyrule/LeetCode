class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = [[]]
        nums.sort()
        for num in nums:
            need_add = []
            for result in results:
                if result + [num] not in results:
                    need_add.append(result + [num])
            results += need_add
        return results