class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums)!=len(list(set(nums)))

if __name__ == '__main__':
    s = Solution()
    nums = [1,5,-2,-4,0]
    r = s.containsDuplicate(nums)
    print(r)