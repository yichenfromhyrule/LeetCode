class Solution(object):
    def binarysearch(self, nums, target, start, end):
        if len(nums)==0 or (end-start==1 and nums[start]!=target):
            return -1
        else:
            mid = (start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return self.binarysearch(nums, target, mid, end)
            elif nums[mid]>target:
                return self.binarysearch(nums, target, start, mid)
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarysearch(nums, target, 0, len(nums))

if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,3,5,9,12]
    target = -7
    r = s.search(nums, target)
    print(r)