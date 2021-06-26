class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target_counts = len(nums)//2
        nums.sort()
        current_value=nums[0]
        current_counts = 1
        if len(nums)==1:
            return nums[0]
        else:
            for i in range(1,len(nums)):
                print("current value is %d and it has %d of them"%(current_value,current_counts))
                if nums[i]==current_value:
                    current_counts+=1
                else:
                    if current_counts>target_counts:
                        return current_value
                    else:
                        current_value=nums[i]
                        current_counts=1
            if current_counts>=target_counts:
                return current_value


if __name__ == '__main__':
    s = Solution()
    nums = [-1,1,1,1,2,1]
    r = s.majorityElement(nums)
    print(r)