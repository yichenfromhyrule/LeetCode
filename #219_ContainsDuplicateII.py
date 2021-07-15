class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        for i in range(0, len(nums)):
            # 1. Check if this num is duplicate
            if nums[i] in hashmap:
                distance = i - hashmap[nums[i]]
                # 1.a. Compare the distance
                if distance <= k:
                    return True
                else:
                    hashmap[nums[i]] = i
            else:
                hashmap[nums[i]] = i
        return False