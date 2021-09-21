class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}
        result = 0
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            else:
                hashmap[num] += 1
        for key in hashmap:
            if hashmap[key] > 0:
                a = (1 + hashmap[key]) * hashmap[key]
                result += (a // 2)
        return result
