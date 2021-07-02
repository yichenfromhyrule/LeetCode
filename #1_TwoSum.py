class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """ Method 1 -- 06/14/2021 -- 6084ms, 14.5MB
        for i in range (0, len(nums)):
            for j in range (0, len(nums)):
                if i<j and nums[i]+nums[j]==target:
                    return [i,j]
        """
        hashmap = {} # Dictionary
        for i in range(0, len(nums)):
            if nums[i] in hashmap:
                    return [hashmap[nums[i]], i]
            else:
                hashmap[target-nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    nums = [0,4,3,0]
    target = 0
    r = s.twoSum(nums, target)
    print(r)