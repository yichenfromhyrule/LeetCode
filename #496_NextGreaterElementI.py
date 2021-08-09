class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums2)):
            hashmap[nums2[i]] = i
        result = [-1 for j in range(len(nums1))]
        for j in range(len(nums1)):
            for check_num in nums2[hashmap[nums1[j]] + 1:]:
                if check_num > nums1[j]:
                    result[j] = check_num
                    break
        return result
