class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # 1. update nums1
        original_nums1 = nums1[:m]
        original_nums2 = nums2
        startIndex=0
        while len(original_nums1)>0 and len(original_nums2)>0:
            num1 = original_nums1[0]
            num2 = original_nums2[0]
            if num1<num2:
                nums1[startIndex]=num1
                startIndex+=1
                original_nums1.pop(0)
            else:
                nums1[startIndex]=num2
                startIndex+=1
                original_nums2.pop(0)
        if len(original_nums1)==0:
            for num in original_nums2:
                nums1[startIndex]=num
                startIndex+=1
        else:
            for num in original_nums1:
                nums1[startIndex]=num
                startIndex+=1



if __name__ == '__main__':
    s = Solution()
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)
