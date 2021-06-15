class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (0, len(nums)):
            for j in range (0, len(nums)):
                if i<j and nums[i]+nums[j]==target:
                    return [i,j]

if __name__ == '__main__':
    s = Solution()
    nums = [3,3]
    target = 6
    r = s.twoSum(nums, target)
    print(r)