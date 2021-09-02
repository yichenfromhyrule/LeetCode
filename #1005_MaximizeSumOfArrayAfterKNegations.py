class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Count num of negative numbers
        nums.sort()
        neg_count = 0
        for num in nums:
            if num <= 0:
                neg_count += 1
            else:
                break
        if k <= neg_count:
            return sum(nums[:k])*(-2) + sum(nums)
        else:
            need = k - neg_count
            if need % 2 == 0:
                return sum(nums[:neg_count])*(-2) + sum(nums)
            else:
                if neg_count < len(nums):
                    min_item = min(abs(nums[neg_count-1]), abs(nums[neg_count]))
                else:
                    min_item = abs(nums[neg_count-1])
                return sum(nums[:neg_count])*(-2) + sum(nums) - 2*min_item