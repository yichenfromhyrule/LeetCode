class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_zero = nums.count(0)
        list_zero = [0 for i in range(num_zero)]
        if nums[-1*num_zero:]!=list_zero:
            found_zero=[]
            for i in range(0, len(nums)):
                if nums[i]==0:
                    found_zero.append(i)
                else:
                    if len(found_zero)>0:
                        nums[found_zero[0]]=nums[i]
                        found_zero.pop(0)
                        nums[i]=0
                        found_zero.append(i)


if __name__ == '__main__':
    s = Solution()
    nums = [2,0,0,7,1,4,11]
    s.moveZeroes(nums)
    print(nums)