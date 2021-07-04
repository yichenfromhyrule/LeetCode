class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        correct_nums = [i for i in range(0, len(nums)+1)]
        nums.sort()
        for m,n in zip(nums,correct_nums[:len(nums)]):
            if m!=n:
                return n
        return correct_nums[len(correct_nums)-1]

if __name__ == '__main__':
    s = Solution()
    nums = [3,0,1]
    r= s.missingNumber(nums)
    print(r)