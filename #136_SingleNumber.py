class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        else:
            nums.sort()
            current_checking = nums[0]
            for i in range(1,len(nums)):
                if nums[i]==current_checking:
                    current_checking=None
                else:
                    if current_checking!=None:
                        return current_checking
                    else:
                        current_checking = nums[i]
            return current_checking


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,3]
    r = s.singleNumber(nums)
    print(r)