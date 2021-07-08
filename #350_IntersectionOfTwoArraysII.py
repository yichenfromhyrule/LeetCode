class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 1. Sort two list
        nums1.sort()
        nums2.sort()
        result = []

        while len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] == nums2[0]:
                result.append(nums1[0])
                nums1.pop(0)
                nums2.pop(0)
            elif nums1[0] < nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)
        return result