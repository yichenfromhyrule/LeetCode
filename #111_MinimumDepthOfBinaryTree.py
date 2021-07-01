# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMinDepth(self, root, minDepth):
        if root!=None:
            minDepth += 1
            if root.left and root.right:
                minDepth = min(self.findMinDepth(root.left, minDepth), self.findMinDepth(root.right, minDepth))
            elif root.left:
                minDepth = self.findMinDepth(root.left, minDepth)
            elif root.right:
                minDepth = self.findMinDepth(root.right, minDepth)
            return minDepth
        else:
            return minDepth

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minDepth = 0
        minDepth = self.findMinDepth(root, minDepth)
        return minDepth