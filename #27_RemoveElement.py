class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            if nums[0]==val:
                nums[0]='_'
                return 0
            else:
                return 1
        else:
            if nums[0]==val:
                nums[0]='_'
            for i in range(1, len(nums)):
                if nums[i]==val:
                    nums[i]='_'
                else:
                    if nums[i-1]=='_':
                        index_symbol = nums.index('_')
                        nums[index_symbol]=nums[i]
                        nums[i]='_'
            return len(nums)-nums.count('_')




if __name__ == '__main__':
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    r = s.removeElement(nums,2)
    print(r)