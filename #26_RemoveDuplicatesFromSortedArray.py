class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 1
        else:
            current_value = nums[0]
            count = 1
            for i in range (1, len(nums)):
                if nums[i]==current_value:
                    nums[i]='_'
                else:
                    if nums[i-1]=='_':
                        if nums[i]!=current_value:
                            current_value = nums[i]
                            first_symbol = nums.index('_')
                            nums[first_symbol]=nums[i]
                            nums[i]="_"

                            count+=1
                        else:
                            nums[i]='_'
                    else:
                        current_value = nums[i]
                        count+=1
        return count


if __name__ == '__main__':
    s = Solution()
    nums = [1]
    r = s.removeDuplicates(nums)
    print(r)