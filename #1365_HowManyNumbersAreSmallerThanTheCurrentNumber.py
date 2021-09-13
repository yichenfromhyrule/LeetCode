class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort_num = sorted(nums)
        hashmap = {}
        for i in range(len(sort_num)):
            if sort_num[i] not in hashmap:
                hashmap[sort_num[i]] = i
        result = []
        for n in nums:
            result.append(hashmap[n])
        return result