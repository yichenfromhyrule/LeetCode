class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        result = []
        new_nums = list(set(nums))
        for new_num in new_nums:
            if (new_num + 1) in hashmap:
                result.append(hashmap[new_num] + hashmap[new_num + 1])
        if len(result) == 0:
            return 0
        else:
            return max(result)
