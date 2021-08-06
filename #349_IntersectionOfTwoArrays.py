class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        if len(nums1) <= len(nums2):
            return self.helperFunction(nums1, nums2)
        else:
            return self.helperFunction(nums2, nums1)

    def helperFunction(self, nums_short, nums_long):
        result = []
        for num in nums_short:
            if num in nums_long:
                result.append(num)
        return result