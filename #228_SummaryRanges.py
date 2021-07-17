class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums.append(2**31+1)
        output = []
        if len(nums) == 0:
            return output
        else:
            result = str(nums[0])
            stack = [nums[0]]
            for i in range(1, len(nums)):
                check_num = stack.pop()
                if nums[i] - 1 == check_num:
                    stack.append(nums[i])
                else:
                    if int(result) != check_num:
                        result = result + "->" + str(check_num)
                    output.append(result)
                    result = str(nums[i])
                    stack = [nums[i]]
        return output