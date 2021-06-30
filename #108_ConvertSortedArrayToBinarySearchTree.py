# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums)==1:
            return TreeNode(nums[0])
        elif len(nums)==2:
            root = TreeNode(nums[0])
            root.right = TreeNode(nums[1])
            return root
        else:
            mid = len(nums)//2
            result = TreeNode(nums[mid])
            if mid-1>= 0:
                result.left = self.sortedArrayToBST(nums[:mid])
            if mid+1<len(nums):
                result.right = self.sortedArrayToBST(nums[mid+1:])
            return result