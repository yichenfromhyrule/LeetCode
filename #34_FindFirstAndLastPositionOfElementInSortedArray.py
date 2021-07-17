class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) > 0:
            result = self.helperFunction(nums, target, 0, len(nums), 10 ** 5 + 1, -1)
            return result if result[0] != 10 ** 5 + 1 else [-1, -1]
        else:
            return [-1, -1]

    def helperFunction(self, nums, target, start, end, r1, r2):
        if end - start > 1:
            # 1. Get mid value in the nums
            mid_index = (start + end) // 2
            if target == nums[mid_index]:
                r1 = mid_index if mid_index < r1 else r1
                r2 = mid_index if mid_index > r2 else r2
                l1 = self.helperFunction(nums, target, start, mid_index, r1, r2)
                l2 = self.helperFunction(nums, target, mid_index, end, r1, r2)
                return [min(l1[0], l2[0]), max(l2[1], l2[1])]
            else:
                if target > nums[mid_index]:
                    return self.helperFunction(nums, target, mid_index, end, r1, r2)
                else:
                    return self.helperFunction(nums, target, start, mid_index, r1, r2)
        else:
            if nums[start] == target:
                r1 = start if r1 > start else r1
                r2 = start if r2 < start else r2
            return [r1, r2]


